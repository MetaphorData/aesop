from typing import Callable, Generic, Iterator, List, Optional, Protocol, TypeVar

from aesop.config import AesopConfig
from aesop.graphql.generated.client import Client

T = TypeVar("T")  # Generic type for the node
R = TypeVar("R", covariant=True)  # Type for the GraphQL response
E = TypeVar("E")  # Type for the edges in the response


class PageInfoProtocol(Protocol):
    end_cursor: Optional[str]
    has_next_page: Optional[bool]


class ClientQueryCallback(Protocol, Generic[R]):
    def __call__(self, client: Client, end_cursor: Optional[str]) -> R: ...  # noqa E704


def paginate_query(
    config: AesopConfig,
    client_query_callback: ClientQueryCallback[R],
    edges_projection: Callable[
        [R], List[Optional[E]]
    ],  # Function to extract edges from the response
    page_info_projection: Callable[
        [R], PageInfoProtocol
    ],  # Function to extract page_info from the response
    edge_to_node: Callable[[E], Optional[T]],  # Function to convert an edge to a node
) -> Iterator[T]:
    client = config.get_graphql_client()
    has_next_page = True
    end_cursor: Optional[str] = None

    while has_next_page:
        # Call the provided query function
        resp = client_query_callback(client=client, end_cursor=end_cursor)

        # Extract edges and page_info using the passed projection functions
        edges = edges_projection(resp)
        page_info = page_info_projection(resp)

        end_cursor = page_info.end_cursor
        has_next_page = page_info.has_next_page or False

        for edge in edges:
            if edge:
                node = edge_to_node(edge)
                if node:
                    yield node

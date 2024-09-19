from aesop.config import AesopConfig
from aesop.graphql.generated.custom_queries import Query


def info(config: AesopConfig) -> None:
    res = config.get_graphql_client().query(Query.crawler_ip_addresses(), operation_name="getCrawlerIpAddresses")
    print(res)
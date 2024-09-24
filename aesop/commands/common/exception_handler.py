import json
from functools import wraps
from typing import Any, Callable, Dict, NoReturn, Tuple, TypeVar, cast

from pydantic import ValidationError as PydanticValidationError

from aesop.commands.common.exceptions import (
    GenericError,
    InvalidAPIKey,
    ValidationError,
)
from aesop.graphql.generated.exceptions import GraphQLClientHttpError

F = TypeVar("F", bound=Callable[..., Any])


def _handle_graphql_client_http_error(
    command: str, e: GraphQLClientHttpError
) -> NoReturn:
    error_payload = json.loads(e.response.text)
    error = error_payload["errors"][0]["message"]
    if error == "Context creation failed: Invalid API key":
        raise InvalidAPIKey(command)
    raise e


def _handle_validation_error(command: str, e: PydanticValidationError) -> NoReturn:
    raise ValidationError(command, e)


def exception_handler(command: str) -> Callable[[F], F]:
    """
    Decorator for methods that need to have exception handling.

    The following exceptions are caught here:
    - GraphQL HTTP client errors
    - Pydantic validation errors
    - BaseExceptions
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> Any:
            try:
                return func(*args, **kwargs)
            except GraphQLClientHttpError as e:
                _handle_graphql_client_http_error(command, e)
            except PydanticValidationError as e:
                _handle_validation_error(command, e)
            except Exception as e:
                raise GenericError(command, e)

        return cast(F, wrapper)

    return decorator

from functools import wraps
from typing import Any, Callable, Dict, Tuple, TypeVar, cast

import typer

from aesop.console import console

F = TypeVar("F", bound=Callable[..., None])


def exception_handler(
    command: str, exception_type: type[Exception], exit_code: int = 1
) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> None:
            try:
                return func(*args, **kwargs)
            except exception_type as e:
                console.error(f"{command.capitalize()}: {str(e)}")
                raise typer.Exit(code=exit_code)

        return cast(F, wrapper)

    return decorator

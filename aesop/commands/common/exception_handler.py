from functools import wraps

import typer

from aesop.console import console


def exception_handler(command: str, exception_type: type[Exception], exit_code: int = 1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type as e:
                console.error(f"{command.upper()}: {str(e)}")
                raise typer.Exit(code=exit_code)

        return wrapper

    return decorator

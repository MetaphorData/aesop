import typing as t

from click import BadParameter, UsageError
from click.core import Context
from pydantic import ValidationError as PydanticValidationError


class InvalidAPIKey(UsageError):
    """
    Exception for when an invalid API key was found.
    """

    def __init__(
        self,
        command: str,
        ctx: t.Optional[Context] = None,
    ) -> None:
        super().__init__(
            f"{command.capitalize()}: Invalid API key. "
            "Please update your configuration file to use an existing API key.",
            ctx,
        )


class ValidationError(BadParameter):
    """
    Exception for when a Pydantic validation error was thrown.
    """

    def __init__(
        self,
        command: str,
        err: PydanticValidationError,
        ctx: t.Optional[Context] = None,
    ) -> None:
        super().__init__(f"{command.capitalize()}: {str(err)}", ctx)


class GenericError(UsageError):
    """
    A generic usage error. Used when a base exception was encountered.
    """

    def __init__(
        self,
        command: str,
        exception: Exception,
        ctx: t.Optional[Context] = None,
    ) -> None:
        super().__init__(f"{command.capitalize()}: {str(exception)}", ctx)

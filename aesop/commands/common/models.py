from abc import ABC, abstractmethod

from pydantic import BaseModel

from aesop.commands.common.enums.output_format import OutputFormat


class InputModel(BaseModel, ABC):
    @staticmethod
    @abstractmethod
    def example_json(indent: int = 0) -> str:
        pass


class OutputModel(BaseModel, ABC):
    @abstractmethod
    def display(self, output: OutputFormat) -> None:
        pass

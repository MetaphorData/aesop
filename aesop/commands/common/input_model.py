from abc import ABC, abstractmethod

from pydantic import BaseModel


class InputModel(BaseModel, ABC):
    @staticmethod
    @abstractmethod
    def example_json() -> str:
        pass

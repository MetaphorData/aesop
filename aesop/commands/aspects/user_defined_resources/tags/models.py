from typing import List, Optional

from pydantic import BaseModel

from aesop import console
from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.models import InputModel, OutputModel


class GovernedTag(BaseModel):
    name: str
    description: Optional[str] = None


class BatchAddTagsInput(InputModel):
    tags: List[GovernedTag]

    @staticmethod
    def example_json(indent: int = 0) -> str:
        return BatchAddTagsInput(
            tags=[
                GovernedTag(
                    name="name of the tag",
                    description=None,
                )
            ]
        ).model_dump_json(indent=indent)


class BatchAssignTagsInput(InputModel):
    tag_ids: List[str]
    asset_ids: List[str]

    @staticmethod
    def example_json(indent: int = 0) -> str:
        return BatchAssignTagsInput(
            tag_ids=[
                "USER_DEFINED_RESOURCE~00000000000000000000000000000001",
                "USER_DEFINED_RESOURCE~00000000000000000000000000000002",
                "USER_DEFINED_RESOURCE~00000000000000000000000000000003",
            ],
            asset_ids=[
                "DATASET~00000000000000000000000000000001",
            ],
        ).model_dump_json(indent=indent)


class BatchRemoveTagsInput(InputModel):
    tag_ids: List[str]

    @staticmethod
    def example_json(indent: int = 0) -> str:
        return BatchRemoveTagsInput(
            tag_ids=[
                "USER_DEFINED_RESOURCE~00000000000000000000000000000001",
                "USER_DEFINED_RESOURCE~00000000000000000000000000000002",
                "USER_DEFINED_RESOURCE~00000000000000000000000000000003",
            ]
        ).model_dump_json(indent=indent)


class AddTagsOutput(OutputModel):
    created_ids: List[str]

    def display(self, output: OutputFormat) -> None:
        if output is OutputFormat.JSON:
            console.console.print(self.model_dump_json())
        else:
            if output is OutputFormat.CSV:
                console.console.warning(
                    "CSV not supported, falling back to showing plain text"
                )
            console.console.print(f"Added tags: {self.created_ids}")


class RemoveTagsOutput(OutputModel):
    removed_ids: List[str]
    failed_ids: List[str]

    def display(self, output: OutputFormat) -> None:
        if output is OutputFormat.JSON:
            console.console.print(self.model_dump_json())
        else:
            if output is OutputFormat.CSV:
                console.console.warning(
                    "CSV not supported, falling back to showing plain text"
                )
            console.console.print(f"Removed tags: {self.removed_ids}")
            if self.failed_ids:
                console.console.warning(f"Failed to delete: {self.failed_ids}")

from typing import List, Optional

from pydantic import BaseModel

from aesop.commands.common.input_model import InputModel


class GovernedTag(BaseModel):
    name: str
    description: Optional[str] = None


class AddTagsInput(InputModel):
    tags: List[GovernedTag]

    @staticmethod
    def example_json(indent: int = 0) -> str:
        return AddTagsInput(
            tags=[
                GovernedTag(
                    name="name of the tag",
                    description=None,
                )
            ]
        ).model_dump_json(indent=indent)


class AssignTagsInput(InputModel):
    tag_ids: List[str]
    asset_ids: List[str]

    @staticmethod
    def example_json(indent: int = 0) -> str:
        return AssignTagsInput(
            tag_ids=[
                "USER_DEFINED_RESOURCE~00000000000000000000000000000001",
                "USER_DEFINED_RESOURCE~00000000000000000000000000000002",
                "USER_DEFINED_RESOURCE~00000000000000000000000000000003",
            ],
            asset_ids=[
                "DATASET~00000000000000000000000000000001",
            ],
        ).model_dump_json(indent=indent)


class RemoveTagsInput(InputModel):
    tag_ids: List[str]

    @staticmethod
    def example_json(indent: int = 0) -> str:
        return RemoveTagsInput(
            tag_ids=[
                "USER_DEFINED_RESOURCE~00000000000000000000000000000001",
                "USER_DEFINED_RESOURCE~00000000000000000000000000000002",
                "USER_DEFINED_RESOURCE~00000000000000000000000000000003",
            ]
        ).model_dump_json(indent=indent)

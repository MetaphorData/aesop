from typing import List, Optional

from pydantic import BaseModel


class GovernedTag(BaseModel):
    name: str
    description: Optional[str] = None


class AddTagsInput(BaseModel):
    tags: List[GovernedTag]


add_tags_input_example = AddTagsInput(
    tags=[
        GovernedTag(
            name="name of the tag",
            description=None,
        )
    ]
)

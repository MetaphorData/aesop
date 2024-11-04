from typing import List

from aesop.commands.common.models import InputModel
from aesop.graphql.generated.enums import DataPlatform
from aesop.graphql.generated.input_types import DatasetPatternInput


class BatchSetNonProdInput(InputModel):
    dataset_patterns: List[DatasetPatternInput]

    @staticmethod
    def example_json(indent: int = 0) -> str:
        return BatchSetNonProdInput(
            dataset_patterns=[
                DatasetPatternInput(
                    database="db",
                    schema="sch",
                    table="*",
                    platform=DataPlatform.SNOWFLAKE,
                    account="john.doe@metaphor.io",
                )
            ]
        ).model_dump_json(indent=indent)

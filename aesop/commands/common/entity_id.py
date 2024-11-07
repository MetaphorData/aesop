import re

from aesop.graphql.generated.enums import EntityType


def is_entity_id(
    x: str,
    entity_type: EntityType,
) -> bool:
    return re.match("^" + entity_type.value + "~[\\dA-F]{32}$", x) is not None

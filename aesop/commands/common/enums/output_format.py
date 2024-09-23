from enum import Enum


class OutputFormat(str, Enum):
    TABULAR = "TABULAR"
    CSV = "CSV"
    JSON = "JSON"

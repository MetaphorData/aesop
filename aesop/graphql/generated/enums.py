# Generated by ariadne-codegen
# Source: schema.gql

from enum import Enum


class APIPlatform(str, Enum):
    OPEN_API = "OPEN_API"
    UNKNOWN = "UNKNOWN"


class AggregationMetadataName(str, Enum):
    Unknown = "Unknown"
    anchorEntityType = "anchorEntityType"
    author = "author"
    authorDisplayName = "authorDisplayName"
    contactDisplayNames = "contactDisplayNames"
    dashboardPlatform = "dashboardPlatform"
    dashboardType = "dashboardType"
    dataPlatform = "dataPlatform"
    dataQuality = "dataQuality"
    database = "database"
    dbtMaterializationType = "dbtMaterializationType"
    dbtTags = "dbtTags"
    department = "department"
    directory = "directory"
    domainDisplayName = "domainDisplayName"
    domainDisplayNames = "domainDisplayNames"
    governedTags = "governedTags"
    hashtags = "hashtags"
    knowledgeCardType = "knowledgeCardType"
    lookerTags = "lookerTags"
    materializationType = "materializationType"
    metricType = "metricType"
    model = "model"
    path = "path"
    pipelineType = "pipelineType"
    platform = "platform"
    project = "project"
    relationship = "relationship"
    schema = "schema"
    snowflakeTags = "snowflakeTags"
    subType = "subType"
    tableauTags = "tableauTags"
    thoughtSpotDataObjectType = "thoughtSpotDataObjectType"
    thoughtSpotTags = "thoughtSpotTags"
    unityCatalogTags = "unityCatalogTags"
    usageLevel = "usageLevel"
    virtualViewType = "virtualViewType"
    workspace = "workspace"


class AnchorEntityType(str, Enum):
    API = "API"
    DASHBOARD = "DASHBOARD"
    DATASET = "DATASET"
    DATA_DOCUMENT = "DATA_DOCUMENT"
    DBT_MODEL = "DBT_MODEL"
    HIERARCHY = "HIERARCHY"
    LOOKER_EXPLORE = "LOOKER_EXPLORE"
    LOOKER_VIEW = "LOOKER_VIEW"
    METRIC = "METRIC"
    PIPELINE = "PIPELINE"
    POWER_BI_DATASET = "POWER_BI_DATASET"
    QUICK_SIGHT = "QUICK_SIGHT"
    TABLEAU_DATASOURCE = "TABLEAU_DATASOURCE"
    THOUGHT_SPOT_DATA_OBJECT = "THOUGHT_SPOT_DATA_OBJECT"


class AppPlatform(str, Enum):
    ChromiumExtension = "ChromiumExtension"
    Email = "Email"
    Slack = "Slack"
    Teams = "Teams"
    Unknown = "Unknown"
    Web = "Web"


class AssetContactValueType(str, Enum):
    EMAIL = "EMAIL"
    GROUP = "GROUP"
    PERSON = "PERSON"
    SLACK = "SLACK"
    UNKNOWN = "UNKNOWN"


class AssetEntityType(str, Enum):
    API = "API"
    DASHBOARD = "DASHBOARD"
    DATASET = "DATASET"
    METRIC = "METRIC"
    PIPELINE = "PIPELINE"
    VIRTUAL_VIEW = "VIRTUAL_VIEW"


class AssetPlatform(str, Enum):
    AIRFLOW = "AIRFLOW"
    ATHENA = "ATHENA"
    AZURE_BLOB_STORAGE = "AZURE_BLOB_STORAGE"
    AZURE_DATA_FACTORY_PIPELINE = "AZURE_DATA_FACTORY_PIPELINE"
    AZURE_DATA_LAKE_STORAGE = "AZURE_DATA_LAKE_STORAGE"
    BIGQUERY = "BIGQUERY"
    CUSTOM = "CUSTOM"
    DASH = "DASH"
    DBT = "DBT"
    DOCUMENTDB = "DOCUMENTDB"
    DYNAMODB = "DYNAMODB"
    ELASTICSEARCH = "ELASTICSEARCH"
    EXTERNAL = "EXTERNAL"
    FIVETRAN = "FIVETRAN"
    GCS = "GCS"
    GLUE = "GLUE"
    HIVE = "HIVE"
    HTTP = "HTTP"
    INFORMATICA = "INFORMATICA"
    KAFKA = "KAFKA"
    LOOKER = "LOOKER"
    METABASE = "METABASE"
    MONGODB = "MONGODB"
    MSSQL = "MSSQL"
    MYSQL = "MYSQL"
    OPEN_API = "OPEN_API"
    ORACLE = "ORACLE"
    POSTGRESQL = "POSTGRESQL"
    POWER_BI = "POWER_BI"
    QUICK_SIGHT = "QUICK_SIGHT"
    RDS = "RDS"
    REDIS = "REDIS"
    REDSHIFT = "REDSHIFT"
    S3 = "S3"
    SFTP = "SFTP"
    SNOWFLAKE = "SNOWFLAKE"
    SPARK = "SPARK"
    SYNAPSE = "SYNAPSE"
    TABLEAU = "TABLEAU"
    THOUGHT_SPOT = "THOUGHT_SPOT"
    TRINO = "TRINO"
    UNITY_CATALOG = "UNITY_CATALOG"
    UNITY_CATALOG_VOLUME_FILE = "UNITY_CATALOG_VOLUME_FILE"
    UNKNOWN = "UNKNOWN"


class AssetRelationType(str, Enum):
    MATERIALIZATION = "MATERIALIZATION"


class AssetSubType(str, Enum):
    AIRFLOW = "AIRFLOW"
    AZURE_DATA_FACTORY_PIPELINE = "AZURE_DATA_FACTORY_PIPELINE"
    CUSTOM_DASHBOARD = "CUSTOM_DASHBOARD"
    DASH_DASHBOARD = "DASH_DASHBOARD"
    DBT_MODEL = "DBT_MODEL"
    EPHEMERAL = "EPHEMERAL"
    EXTERNAL = "EXTERNAL"
    FIVETRAN = "FIVETRAN"
    GENERIC_DATASET = "GENERIC_DATASET"
    GENERIC_METRIC = "GENERIC_METRIC"
    INCREMENTAL = "INCREMENTAL"
    INFORMATICA_MAPPING = "INFORMATICA_MAPPING"
    LOOKER_DASHBOARD = "LOOKER_DASHBOARD"
    LOOKER_EXPLORE = "LOOKER_EXPLORE"
    LOOKER_VIEW = "LOOKER_VIEW"
    MATERIALIZED_VIEW = "MATERIALIZED_VIEW"
    METABASE_DASHBOARD = "METABASE_DASHBOARD"
    OTHER = "OTHER"
    POWER_BI_DASHBOARD = "POWER_BI_DASHBOARD"
    POWER_BI_DATAFLOW = "POWER_BI_DATAFLOW"
    POWER_BI_DATASET = "POWER_BI_DATASET"
    POWER_BI_REPORT = "POWER_BI_REPORT"
    QUICK_SIGHT = "QUICK_SIGHT"
    QUICK_SIGHT_DASHBOARD = "QUICK_SIGHT_DASHBOARD"
    SNAPSHOT = "SNAPSHOT"
    SPARK = "SPARK"
    STREAM = "STREAM"
    TABLE = "TABLE"
    TABLEAU_DASHBOARD = "TABLEAU_DASHBOARD"
    TABLEAU_DATASOURCE = "TABLEAU_DATASOURCE"
    THOUGHT_SPOT_ANSWER = "THOUGHT_SPOT_ANSWER"
    THOUGHT_SPOT_DASHBOARD = "THOUGHT_SPOT_DASHBOARD"
    THOUGHT_SPOT_DATA_OBJECT = "THOUGHT_SPOT_DATA_OBJECT"
    THOUGHT_SPOT_LIVEBOARD = "THOUGHT_SPOT_LIVEBOARD"
    UNITY_CATALOG_EXTERNAL_LOCATION = "UNITY_CATALOG_EXTERNAL_LOCATION"
    UNITY_CATALOG_TABLE = "UNITY_CATALOG_TABLE"
    UNITY_CATALOG_VOLUME = "UNITY_CATALOG_VOLUME"
    UNITY_CATALOG_VOLUME_FILE = "UNITY_CATALOG_VOLUME_FILE"
    UNKNOWN = "UNKNOWN"
    UNKNOWN_DASHBOARD = "UNKNOWN_DASHBOARD"
    VIEW = "VIEW"
    WORKSHEET = "WORKSHEET"


class BrowsePathSegmentType(str, Enum):
    COLLECTION = "COLLECTION"
    DASHBOARD = "DASHBOARD"
    DATABASE = "DATABASE"
    DATASET = "DATASET"
    DIRECTORY = "DIRECTORY"
    EXPLORE = "EXPLORE"
    METRIC = "METRIC"
    MODEL = "MODEL"
    NAMESPACE = "NAMESPACE"
    OPEN_API_SECTION = "OPEN_API_SECTION"
    OPEN_API_SPEC = "OPEN_API_SPEC"
    PIPELINE = "PIPELINE"
    PLATFORM = "PLATFORM"
    POWER_BI_DATASET = "POWER_BI_DATASET"
    PROJECT = "PROJECT"
    QUICK_SIGHT = "QUICK_SIGHT"
    SCHEMA = "SCHEMA"
    TABLEAU_DATASOURCE = "TABLEAU_DATASOURCE"
    THOUGHT_SPOT_DASHBOARD = "THOUGHT_SPOT_DASHBOARD"
    THOUGHT_SPOT_DATA_OBJECT = "THOUGHT_SPOT_DATA_OBJECT"
    TYPE = "TYPE"
    UNKNOWN = "UNKNOWN"
    VIEW = "VIEW"
    WORKSPACE = "WORKSPACE"


class ChangeRequestStatus(str, Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"


class ChangeRequestType(str, Enum):
    ASSET_ACCESS = "ASSET_ACCESS"
    COLUMN_UPDATE = "COLUMN_UPDATE"
    CONTACTS_UPDATE = "CONTACTS_UPDATE"
    CONTENT_UPDATE = "CONTENT_UPDATE"
    CURATE_QUERY = "CURATE_QUERY"
    DESCRIPTION_UPDATE = "DESCRIPTION_UPDATE"
    TAGS_UPDATE = "TAGS_UPDATE"
    UNKNOWN = "UNKNOWN"


class ChartType(str, Enum):
    AREA = "AREA"
    BAR = "BAR"
    BOX_PLOT = "BOX_PLOT"
    COLUMN = "COLUMN"
    DONUT = "DONUT"
    FUNNEL = "FUNNEL"
    LINE = "LINE"
    MAP = "MAP"
    OTHER = "OTHER"
    PIE = "PIE"
    SCATTER = "SCATTER"
    TABLE = "TABLE"
    TEXT = "TEXT"
    TIMELINE = "TIMELINE"
    UNKNOWN = "UNKNOWN"
    WATERFALL = "WATERFALL"


class CrawlerLatestStatus(str, Enum):
    INITIALIZING = "INITIALIZING"
    NOT_STARTED = "NOT_STARTED"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"


class CrawlerType(str, Enum):
    ATHENA = "ATHENA"
    AZURE_DATA_FACTORY = "AZURE_DATA_FACTORY"
    BIGQUERY = "BIGQUERY"
    BIGQUERY_LINEAGE = "BIGQUERY_LINEAGE"
    BIGQUERY_PROFILE = "BIGQUERY_PROFILE"
    CONFLUENCE = "CONFLUENCE"
    DATAHUB = "DATAHUB"
    DBT = "DBT"
    DBT_CLOUD = "DBT_CLOUD"
    FIVETRAN = "FIVETRAN"
    GLUE = "GLUE"
    HIVE = "HIVE"
    INFORMATICA = "INFORMATICA"
    KAFKA = "KAFKA"
    LOOKER = "LOOKER"
    METABASE = "METABASE"
    MONDAY = "MONDAY"
    MONGODB = "MONGODB"
    MONTE_CARLO = "MONTE_CARLO"
    MSSQL = "MSSQL"
    MYSQL = "MYSQL"
    NOTION = "NOTION"
    OPEN_API = "OPEN_API"
    ORACLE = "ORACLE"
    POSTGRESQL = "POSTGRESQL"
    POSTGRESQL_PROFILE = "POSTGRESQL_PROFILE"
    POWER_BI = "POWER_BI"
    QUICK_SIGHT = "QUICK_SIGHT"
    REDSHIFT = "REDSHIFT"
    REDSHIFT_PROFILE = "REDSHIFT_PROFILE"
    S3 = "S3"
    SHAREPOINT = "SHAREPOINT"
    SNOWFLAKE = "SNOWFLAKE"
    SNOWFLAKE_PROFILE = "SNOWFLAKE_PROFILE"
    STATIC_WEB = "STATIC_WEB"
    SYNAPSE = "SYNAPSE"
    TABLEAU = "TABLEAU"
    THOUGHTSPOT = "THOUGHTSPOT"
    TRINO = "TRINO"
    UNITY_CATALOG = "UNITY_CATALOG"
    UNITY_CATALOG_PROFILE = "UNITY_CATALOG_PROFILE"
    UNKNOWN = "UNKNOWN"


class CustomMetadataDataType(str, Enum):
    ARRAY_OF_NUMBER = "ARRAY_OF_NUMBER"
    ARRAY_OF_STRING = "ARRAY_OF_STRING"
    BOOLEAN = "BOOLEAN"
    NUMBER = "NUMBER"
    OBJECT = "OBJECT"
    STRING = "STRING"


class DashboardPlatform(str, Enum):
    CUSTOM_DASHBOARD = "CUSTOM_DASHBOARD"
    DASH = "DASH"
    LOOKER = "LOOKER"
    METABASE = "METABASE"
    POWER_BI = "POWER_BI"
    QUICK_SIGHT = "QUICK_SIGHT"
    TABLEAU = "TABLEAU"
    THOUGHT_SPOT = "THOUGHT_SPOT"
    UNKNOWN = "UNKNOWN"


class DashboardType(str, Enum):
    POWER_BI_DASHBOARD = "POWER_BI_DASHBOARD"
    POWER_BI_REPORT = "POWER_BI_REPORT"
    THOUGHT_SPOT_ANSWER = "THOUGHT_SPOT_ANSWER"
    THOUGHT_SPOT_LIVEBOARD = "THOUGHT_SPOT_LIVEBOARD"
    UNKNOWN = "UNKNOWN"


class DataMonitorSeverity(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    UNKNOWN = "UNKNOWN"


class DataMonitorStatus(str, Enum):
    ERROR = "ERROR"
    PASSED = "PASSED"
    UNKNOWN = "UNKNOWN"
    WARNING = "WARNING"


class DataPlatform(str, Enum):
    ATHENA = "ATHENA"
    AZURE_BLOB_STORAGE = "AZURE_BLOB_STORAGE"
    AZURE_DATA_LAKE_STORAGE = "AZURE_DATA_LAKE_STORAGE"
    BIGQUERY = "BIGQUERY"
    DOCUMENTDB = "DOCUMENTDB"
    DYNAMODB = "DYNAMODB"
    ELASTICSEARCH = "ELASTICSEARCH"
    EXTERNAL = "EXTERNAL"
    GCS = "GCS"
    GLUE = "GLUE"
    HIVE = "HIVE"
    HTTP = "HTTP"
    KAFKA = "KAFKA"
    MONGODB = "MONGODB"
    MSSQL = "MSSQL"
    MYSQL = "MYSQL"
    ORACLE = "ORACLE"
    POSTGRESQL = "POSTGRESQL"
    RDS = "RDS"
    REDIS = "REDIS"
    REDSHIFT = "REDSHIFT"
    S3 = "S3"
    SFTP = "SFTP"
    SNOWFLAKE = "SNOWFLAKE"
    SYNAPSE = "SYNAPSE"
    TRINO = "TRINO"
    UNITY_CATALOG = "UNITY_CATALOG"
    UNITY_CATALOG_VOLUME_FILE = "UNITY_CATALOG_VOLUME_FILE"
    UNKNOWN = "UNKNOWN"


class DataQualityProvider(str, Enum):
    BIGEYE = "BIGEYE"
    DBT = "DBT"
    GREAT_EXPECTATIONS = "GREAT_EXPECTATIONS"
    LIGHTUP = "LIGHTUP"
    MONTE_CARLO = "MONTE_CARLO"
    SODA = "SODA"
    UNKNOWN = "UNKNOWN"


class DataQualityStatus(str, Enum):
    CAUTION = "CAUTION"
    FAIL = "FAIL"
    NO_STATUS = "NO_STATUS"
    PASSED = "PASSED"
    WARNING = "WARNING"


class DbtMaterializationType(str, Enum):
    EPHEMERAL = "EPHEMERAL"
    INCREMENTAL = "INCREMENTAL"
    OTHER = "OTHER"
    SNAPSHOT = "SNAPSHOT"
    TABLE = "TABLE"
    VIEW = "VIEW"


class DependencyCondition(str, Enum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"
    SUCCEEDED = "SUCCEEDED"


class EntityType(str, Enum):
    API = "API"
    DASHBOARD = "DASHBOARD"
    DATASET = "DATASET"
    GROUP = "GROUP"
    HIERARCHY = "HIERARCHY"
    KNOWLEDGE_CARD = "KNOWLEDGE_CARD"
    METRIC = "METRIC"
    NAMESPACE = "NAMESPACE"
    PERSON = "PERSON"
    PIPELINE = "PIPELINE"
    USER_DEFINED_RESOURCE = "USER_DEFINED_RESOURCE"
    VIRTUAL_VIEW = "VIRTUAL_VIEW"


class GroupPlatform(str, Enum):
    AZURE_AD = "AZURE_AD"
    METAPHOR = "METAPHOR"
    OKTA = "OKTA"


class HierarchyType(str, Enum):
    LOOKER_FOLDER = "LOOKER_FOLDER"
    METABASE_COLLECTION = "METABASE_COLLECTION"
    OPEN_API = "OPEN_API"
    POWER_BI_WORKSPACE = "POWER_BI_WORKSPACE"
    THOUGHT_SPOT_VIRTUAL_HIERARCHY = "THOUGHT_SPOT_VIRTUAL_HIERARCHY"
    UNKNOWN = "UNKNOWN"
    VIRTUAL_HIERARCHY = "VIRTUAL_HIERARCHY"


class InAppOnboardingCompletionStep(str, Enum):
    InstalledBrowserExtension = "InstalledBrowserExtension"
    InstalledChatClientApp = "InstalledChatClientApp"
    WatchedGetStartedVideo = "WatchedGetStartedVideo"


class InAppProfileCompletionStep(str, Enum):
    InvitedTeammates = "InvitedTeammates"


class InterestedPartySource(str, Enum):
    Author = "Author"
    Follower = "Follower"
    Mentioned = "Mentioned"
    QueriedBy = "QueriedBy"
    Unknown = "Unknown"


class KnowledgeCardState(str, Enum):
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"


class KnowledgeCardType(str, Enum):
    ASSET_DESCRIPTION = "ASSET_DESCRIPTION"
    CHANGE_REQUEST = "CHANGE_REQUEST"
    COLUMN_DESCRIPTION = "COLUMN_DESCRIPTION"
    COMMENT = "COMMENT"
    DATA_DOCUMENT = "DATA_DOCUMENT"
    DEPRECATION = "DEPRECATION"
    HOW_TO_USE = "HOW_TO_USE"
    INCIDENT = "INCIDENT"
    QUERY_DESCRIPTION = "QUERY_DESCRIPTION"
    UNKNOWN = "UNKNOWN"


class LineageType(str, Enum):
    API = "API"
    DASHBOARD = "DASHBOARD"
    DATASET = "DATASET"
    DBT_MODEL = "DBT_MODEL"
    LOOKER_EXPLORE = "LOOKER_EXPLORE"
    LOOKER_VIEW = "LOOKER_VIEW"
    METRIC = "METRIC"
    POWER_BI_DATASET = "POWER_BI_DATASET"
    QUICK_SIGHT = "QUICK_SIGHT"
    TABLEAU_DATASOURCE = "TABLEAU_DATASOURCE"
    THOUGHT_SPOT_DATA_OBJECT = "THOUGHT_SPOT_DATA_OBJECT"


class MaterializationType(str, Enum):
    EXTERNAL = "EXTERNAL"
    MATERIALIZED_VIEW = "MATERIALIZED_VIEW"
    SNAPSHOT = "SNAPSHOT"
    STREAM = "STREAM"
    TABLE = "TABLE"
    VIEW = "VIEW"


class MetricType(str, Enum):
    DBT_METRIC = "DBT_METRIC"
    UNKNOWN = "UNKNOWN"


class NamespaceType(str, Enum):
    DATA_GROUP = "DATA_GROUP"
    DATA_UNIT = "DATA_UNIT"
    PERSONAL_SPACE = "PERSONAL_SPACE"
    UNKNOWN = "UNKNOWN"
    USER_DEFINED_SPACE = "USER_DEFINED_SPACE"


class NativeType(str, Enum):
    AIRFLOW = "AIRFLOW"
    ASSET_CONTACT = "ASSET_CONTACT"
    ASSET_DESCRIPTION = "ASSET_DESCRIPTION"
    ATHENA = "ATHENA"
    AZURE_BLOB_STORAGE = "AZURE_BLOB_STORAGE"
    AZURE_DATA_FACTORY_PIPELINE = "AZURE_DATA_FACTORY_PIPELINE"
    AZURE_DATA_LAKE_STORAGE = "AZURE_DATA_LAKE_STORAGE"
    BIGEYE = "BIGEYE"
    BIGQUERY = "BIGQUERY"
    CHANGE_REQUEST = "CHANGE_REQUEST"
    COLUMN_DESCRIPTION = "COLUMN_DESCRIPTION"
    COMMENT = "COMMENT"
    COMMON_COLUMN_ATTRIBUTES = "COMMON_COLUMN_ATTRIBUTES"
    CONFLUENCE = "CONFLUENCE"
    CUSTOM = "CUSTOM"
    CUSTOM_DASHBOARD = "CUSTOM_DASHBOARD"
    DASH = "DASH"
    DATAHUB = "DATAHUB"
    DATA_DOCUMENT = "DATA_DOCUMENT"
    DATA_GROUP = "DATA_GROUP"
    DATA_UNIT = "DATA_UNIT"
    DBT = "DBT"
    DBT_METRIC = "DBT_METRIC"
    DBT_MODEL = "DBT_MODEL"
    DEPRECATION = "DEPRECATION"
    DOCUMENTDB = "DOCUMENTDB"
    DYNAMODB = "DYNAMODB"
    ELASTICSEARCH = "ELASTICSEARCH"
    EXTERNAL = "EXTERNAL"
    FIVETRAN = "FIVETRAN"
    GCS = "GCS"
    GLUE = "GLUE"
    GOVERNED_TAG = "GOVERNED_TAG"
    GREAT_EXPECTATIONS = "GREAT_EXPECTATIONS"
    HIVE = "HIVE"
    HOW_TO_USE = "HOW_TO_USE"
    HTTP = "HTTP"
    INCIDENT = "INCIDENT"
    INFORMATICA = "INFORMATICA"
    INFORMATICA_MAPPING = "INFORMATICA_MAPPING"
    KAFKA = "KAFKA"
    LIGHTUP = "LIGHTUP"
    LOOKER = "LOOKER"
    LOOKER_EXPLORE = "LOOKER_EXPLORE"
    LOOKER_VIEW = "LOOKER_VIEW"
    METABASE = "METABASE"
    MONDAY = "MONDAY"
    MONGODB = "MONGODB"
    MONTE_CARLO = "MONTE_CARLO"
    MSSQL = "MSSQL"
    MYSQL = "MYSQL"
    NOTION = "NOTION"
    OPEN_API = "OPEN_API"
    ORACLE = "ORACLE"
    PERSONAL_SPACE = "PERSONAL_SPACE"
    POSTGRESQL = "POSTGRESQL"
    POWER_BI = "POWER_BI"
    POWER_BI_DATAFLOW = "POWER_BI_DATAFLOW"
    POWER_BI_DATASET = "POWER_BI_DATASET"
    QUERY_DESCRIPTION = "QUERY_DESCRIPTION"
    QUICK_SIGHT = "QUICK_SIGHT"
    RDS = "RDS"
    REDIS = "REDIS"
    REDSHIFT = "REDSHIFT"
    S3 = "S3"
    SFTP = "SFTP"
    SHAREPOINT = "SHAREPOINT"
    SNOWFLAKE = "SNOWFLAKE"
    SODA = "SODA"
    SPARK = "SPARK"
    STATIC_WEB = "STATIC_WEB"
    SYNAPSE = "SYNAPSE"
    TABLEAU = "TABLEAU"
    TABLEAU_DATASOURCE = "TABLEAU_DATASOURCE"
    THOUGHT_SPOT = "THOUGHT_SPOT"
    THOUGHT_SPOT_DATA_OBJECT = "THOUGHT_SPOT_DATA_OBJECT"
    TRINO = "TRINO"
    UNITY_CATALOG = "UNITY_CATALOG"
    UNITY_CATALOG_VOLUME_FILE = "UNITY_CATALOG_VOLUME_FILE"
    UNKNOWN = "UNKNOWN"
    USER_DEFINED_SPACE = "USER_DEFINED_SPACE"


class Order(str, Enum):
    Asc = "Asc"
    Desc = "Desc"


class Persona(str, Enum):
    DATA_CONSUMER = "DATA_CONSUMER"
    DATA_PRODUCER = "DATA_PRODUCER"


class PipelineType(str, Enum):
    AIRFLOW = "AIRFLOW"
    AZURE_DATA_FACTORY_PIPELINE = "AZURE_DATA_FACTORY_PIPELINE"
    FIVETRAN = "FIVETRAN"
    INFORMATICA_MAPPING = "INFORMATICA_MAPPING"
    POWER_BI_DATAFLOW = "POWER_BI_DATAFLOW"
    SPARK = "SPARK"
    UNKNOWN = "UNKNOWN"


class PlatformType(str, Enum):
    AIRFLOW = "AIRFLOW"
    ATHENA = "ATHENA"
    AZURE_BLOB_STORAGE = "AZURE_BLOB_STORAGE"
    AZURE_DATA_FACTORY_PIPELINE = "AZURE_DATA_FACTORY_PIPELINE"
    AZURE_DATA_LAKE_STORAGE = "AZURE_DATA_LAKE_STORAGE"
    BIGEYE = "BIGEYE"
    BIGQUERY = "BIGQUERY"
    CONFLUENCE = "CONFLUENCE"
    CUSTOM = "CUSTOM"
    CUSTOM_DASHBOARD = "CUSTOM_DASHBOARD"
    DASH = "DASH"
    DATAHUB = "DATAHUB"
    DBT = "DBT"
    DBT_METRIC = "DBT_METRIC"
    DBT_MODEL = "DBT_MODEL"
    DOCUMENTDB = "DOCUMENTDB"
    DYNAMODB = "DYNAMODB"
    ELASTICSEARCH = "ELASTICSEARCH"
    EXTERNAL = "EXTERNAL"
    FIVETRAN = "FIVETRAN"
    GCS = "GCS"
    GLUE = "GLUE"
    GREAT_EXPECTATIONS = "GREAT_EXPECTATIONS"
    HIVE = "HIVE"
    HTTP = "HTTP"
    INFORMATICA = "INFORMATICA"
    INFORMATICA_MAPPING = "INFORMATICA_MAPPING"
    KAFKA = "KAFKA"
    LIGHTUP = "LIGHTUP"
    LOOKER = "LOOKER"
    LOOKER_EXPLORE = "LOOKER_EXPLORE"
    LOOKER_VIEW = "LOOKER_VIEW"
    METABASE = "METABASE"
    MONDAY = "MONDAY"
    MONGODB = "MONGODB"
    MONTE_CARLO = "MONTE_CARLO"
    MSSQL = "MSSQL"
    MYSQL = "MYSQL"
    NOTION = "NOTION"
    OPEN_API = "OPEN_API"
    ORACLE = "ORACLE"
    POSTGRESQL = "POSTGRESQL"
    POWER_BI = "POWER_BI"
    POWER_BI_DATAFLOW = "POWER_BI_DATAFLOW"
    POWER_BI_DATASET = "POWER_BI_DATASET"
    QUICK_SIGHT = "QUICK_SIGHT"
    RDS = "RDS"
    REDIS = "REDIS"
    REDSHIFT = "REDSHIFT"
    S3 = "S3"
    SFTP = "SFTP"
    SHAREPOINT = "SHAREPOINT"
    SNOWFLAKE = "SNOWFLAKE"
    SODA = "SODA"
    SPARK = "SPARK"
    STATIC_WEB = "STATIC_WEB"
    SYNAPSE = "SYNAPSE"
    TABLEAU = "TABLEAU"
    TABLEAU_DATASOURCE = "TABLEAU_DATASOURCE"
    THOUGHT_SPOT = "THOUGHT_SPOT"
    THOUGHT_SPOT_DATA_OBJECT = "THOUGHT_SPOT_DATA_OBJECT"
    TRINO = "TRINO"
    UNITY_CATALOG = "UNITY_CATALOG"
    UNITY_CATALOG_VOLUME_FILE = "UNITY_CATALOG_VOLUME_FILE"
    UNKNOWN = "UNKNOWN"


class PowerBiDashboardType(str, Enum):
    DASHBOARD = "DASHBOARD"
    REPORT = "REPORT"


class PowerBiEndorsementType(str, Enum):
    CERTIFIED = "CERTIFIED"
    NONE = "NONE"
    PROMOTED = "PROMOTED"


class PowerBiWorkspaceAccessRight(str, Enum):
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"
    VIEWER = "VIEWER"


class QueryDescriptionSupportedStatement(str, Enum):
    DELETE = "DELETE"
    INSERT = "INSERT"
    SELECT = "SELECT"
    UPDATE = "UPDATE"


class QueryDescriptionType(str, Enum):
    Business = "Business"
    Freeform = "Freeform"
    Technical = "Technical"


class RunStatus(str, Enum):
    FAILURE = "FAILURE"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"


class SchemaType(str, Enum):
    AVRO = "AVRO"
    BSON = "BSON"
    DYNAMODB = "DYNAMODB"
    JSON = "JSON"
    ORC = "ORC"
    PARQUET = "PARQUET"
    PROTOBUF = "PROTOBUF"
    SCHEMALESS = "SCHEMALESS"
    SQL = "SQL"


class SearchContext(str, Enum):
    API = "API"
    Assets = "Assets"
    DATA_DOCUMENT = "DATA_DOCUMENT"
    DATA_GROUP = "DATA_GROUP"
    DBT_MODEL = "DBT_MODEL"
    Dashboards = "Dashboards"
    Datasets = "Datasets"
    Groups = "Groups"
    KnowledgeCards = "KnowledgeCards"
    LOOKER_EXPLORE = "LOOKER_EXPLORE"
    LOOKER_VIEW = "LOOKER_VIEW"
    Metrics = "Metrics"
    POWER_BI_DATASET = "POWER_BI_DATASET"
    Persons = "Persons"
    Pipelines = "Pipelines"
    QUICK_SIGHT = "QUICK_SIGHT"
    TABLEAU_DATASOURCE = "TABLEAU_DATASOURCE"
    THOUGHT_SPOT_DATA_OBJECT = "THOUGHT_SPOT_DATA_OBJECT"


class SearchIndex(str, Enum):
    Assets = "Assets"
    Dashboards = "Dashboards"
    DatasetColumns = "DatasetColumns"
    Datasets = "Datasets"
    Groups = "Groups"
    Hierarchies = "Hierarchies"
    KnowledgeCards = "KnowledgeCards"
    Metrics = "Metrics"
    Namespaces = "Namespaces"
    Persons = "Persons"
    Pipelines = "Pipelines"
    UserDefinedResource = "UserDefinedResource"
    VirtualViews = "VirtualViews"


class SnowflakeIcebergTableType(str, Enum):
    MANAGED = "MANAGED"
    NOT_ICEBERG = "NOT_ICEBERG"
    UNKNOWN = "UNKNOWN"
    UNMANAGED = "UNMANAGED"


class SnowflakeStreamSourceType(str, Enum):
    TABLE = "TABLE"
    UNKNOWN = "UNKNOWN"
    VIEW = "VIEW"


class SnowflakeStreamType(str, Enum):
    APPEND_ONLY = "APPEND_ONLY"
    INSERT_ONLY = "INSERT_ONLY"
    STANDARD = "STANDARD"
    UNKNOWN = "UNKNOWN"


class SystemTagSource(str, Enum):
    DATAHUB = "DATAHUB"
    DBT = "DBT"
    LOOKER = "LOOKER"
    SNOWFLAKE = "SNOWFLAKE"
    TABLEAU = "TABLEAU"
    THOUGHT_SPOT = "THOUGHT_SPOT"
    UNITY_CATALOG = "UNITY_CATALOG"
    UNKNOWN = "UNKNOWN"


class TenantStatus(str, Enum):
    DELETED = "DELETED"
    DELETING = "DELETING"
    ERROR = "ERROR"
    OK = "OK"
    UNKNOWN = "UNKNOWN"
    UPDATING = "UPDATING"


class ThoughtSpotDashboardType(str, Enum):
    ANSWER = "ANSWER"
    LIVEBOARD = "LIVEBOARD"
    UNKNOWN = "UNKNOWN"


class ThoughtSpotDataObjectType(str, Enum):
    TABLE = "TABLE"
    UNKNOWN = "UNKNOWN"
    VIEW = "VIEW"
    WORKSHEET = "WORKSHEET"


class UnityCatalogDatasetType(str, Enum):
    UNITY_CATALOG_EXTERNAL_LOCATION = "UNITY_CATALOG_EXTERNAL_LOCATION"
    UNITY_CATALOG_TABLE = "UNITY_CATALOG_TABLE"
    UNITY_CATALOG_VOLUME = "UNITY_CATALOG_VOLUME"
    UNITY_CATALOG_VOLUME_FILE = "UNITY_CATALOG_VOLUME_FILE"
    UNKNOWN = "UNKNOWN"


class UnityCatalogTableType(str, Enum):
    EXTERNAL = "EXTERNAL"
    EXTERNAL_SHALLOW_CLONE = "EXTERNAL_SHALLOW_CLONE"
    FOREIGN = "FOREIGN"
    MANAGED = "MANAGED"
    MANAGED_SHALLOW_CLONE = "MANAGED_SHALLOW_CLONE"
    MATERIALIZED_VIEW = "MATERIALIZED_VIEW"
    STREAMING_TABLE = "STREAMING_TABLE"
    UNKNOWN = "UNKNOWN"
    VIEW = "VIEW"


class UnityCatalogVolumeType(str, Enum):
    EXTERNAL = "EXTERNAL"
    MANAGED = "MANAGED"
    UNKNOWN = "UNKNOWN"


class UsageLevel(str, Enum):
    High = "High"
    Low = "Low"
    Medium = "Medium"
    None_ = "None"


class UserActivityGranularity(str, Enum):
    DAILY = "DAILY"
    HOURLY = "HOURLY"
    MONTHLY = "MONTHLY"


class UserActivitySource(str, Enum):
    APP = "APP"
    POWER_BI = "POWER_BI"
    UNKNOWN = "UNKNOWN"


class UserActivityType(str, Enum):
    SUBSCRIBE = "SUBSCRIBE"
    UNKNOWN = "UNKNOWN"
    VIEW = "VIEW"


class UserDefinedOrderType(str, Enum):
    GLOBAL_DATA_GROUP_OR_UNIT = "GLOBAL_DATA_GROUP_OR_UNIT"
    UNKNOWN = "UNKNOWN"


class UserDefinedResourceType(str, Enum):
    ASSET_CONTACT = "ASSET_CONTACT"
    COMMON_COLUMN_ATTRIBUTES = "COMMON_COLUMN_ATTRIBUTES"
    GOVERNED_TAG = "GOVERNED_TAG"
    UNKNOWN = "UNKNOWN"


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    API_KEY = "API_KEY"
    CONTRIBUTOR = "CONTRIBUTOR"
    DATA_ADMIN = "DATA_ADMIN"
    TECH_SUPPORT = "TECH_SUPPORT"


class VersionUpdateField(str, Enum):
    activity = "activity"
    assetContacts = "assetContacts"
    assetFollowers = "assetFollowers"
    assetGovernedTags = "assetGovernedTags"
    assetLikes = "assetLikes"
    azureDataFactoryPipeline = "azureDataFactoryPipeline"
    commonColumnAttributes = "commonColumnAttributes"
    createdAt = "createdAt"
    customMetadata = "customMetadata"
    dashboardInfo = "dashboardInfo"
    dataQuality = "dataQuality"
    dbtMetric = "dbtMetric"
    dbtModel = "dbtModel"
    deletedAt = "deletedAt"
    displayName = "displayName"
    documentation = "documentation"
    entityType = "entityType"
    entityUpstream = "entityUpstream"
    fieldAssociations = "fieldAssociations"
    fieldStatistics = "fieldStatistics"
    fivetran = "fivetran"
    groupInfo = "groupInfo"
    informaticaMapping = "informaticaMapping"
    knowledgeCardInfo = "knowledgeCardInfo"
    lastIngestedAt = "lastIngestedAt"
    lastModifiedAt = "lastModifiedAt"
    lastQuery = "lastQuery"
    logicalId = "logicalId"
    lookerExplore = "lookerExplore"
    lookerView = "lookerView"
    metricInfo = "metricInfo"
    namespaceAssets = "namespaceAssets"
    namespaceInfo = "namespaceInfo"
    organization = "organization"
    overallDataQuality = "overallDataQuality"
    parsedUpstream = "parsedUpstream"
    personalization = "personalization"
    pinnedAssets = "pinnedAssets"
    pipelineInfo = "pipelineInfo"
    powerBIDataset = "powerBIDataset"
    powerBiDataflow = "powerBiDataflow"
    properties = "properties"
    quickSight = "quickSight"
    relatedAssets = "relatedAssets"
    schema = "schema"
    scimProfile = "scimProfile"
    slackProfile = "slackProfile"
    snowflakeIcebergInfo = "snowflakeIcebergInfo"
    snowflakeStreamInfo = "snowflakeStreamInfo"
    sodaDataQuality = "sodaDataQuality"
    sourceInfo = "sourceInfo"
    spark = "spark"
    statistics = "statistics"
    structure = "structure"
    systemContacts = "systemContacts"
    systemDescription = "systemDescription"
    systemTags = "systemTags"
    tableauDatasource = "tableauDatasource"
    teamsConversionReference = "teamsConversionReference"
    thoughtSpot = "thoughtSpot"
    unityCatalog = "unityCatalog"
    usage = "usage"
    userDefinedResourceInfo = "userDefinedResourceInfo"


class VirtualViewType(str, Enum):
    DBT_MODEL = "DBT_MODEL"
    LOOKER_EXPLORE = "LOOKER_EXPLORE"
    LOOKER_VIEW = "LOOKER_VIEW"
    POWER_BI_DATASET = "POWER_BI_DATASET"
    QUICK_SIGHT = "QUICK_SIGHT"
    TABLEAU_DATASOURCE = "TABLEAU_DATASOURCE"
    THOUGHT_SPOT_DATA_OBJECT = "THOUGHT_SPOT_DATA_OBJECT"
    UNKNOWN = "UNKNOWN"


class WebhookTriggerType(str, Enum):
    DATASET_SCHEMA_CHANGED = "DATASET_SCHEMA_CHANGED"
    SERVICE_REQUEST_CREATED = "SERVICE_REQUEST_CREATED"
    UNKNOWN = "UNKNOWN"

# Metaphor CLI Documentation

**Usage**:

```console
$ aesop [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--check-newer-version / --no-check-newer-version`: [default: check-newer-version]
* `--config-file FILENAME`: Path to the configuration file.  [default: /Users/andy/.aesop/config.yml]
* `--help`: Show this message and exit.

**Commands**:

* `datasets`: Manage datasets in Metaphor.
* `documents`: Manages data documents on Metaphor.
* `domains`: Manages data domains in Metaphor.
* `glossaries`: Manages glossary documents.
* `help`: Print help for a command.
* `info`: Display information about the Metaphor...
* `settings`: Manage settings in Metaphor.
* `tags`: Manage tags in Metaphor.
* `upload`: Upload data assets from a CSV file.
* `version`: Print Aesop's version.
* `webhooks`: Manages webhooks.

## `aesop datasets`

Manage datasets in Metaphor.

**Usage**:

```console
$ aesop datasets [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get-aspect`: Display aspect of a dataset in Metaphor.

### `aesop datasets get-aspect`

Display aspect of a dataset in Metaphor.

**Usage**:

```console
$ aesop datasets get-aspect [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `governed-tags`: Show governed tags this dataset is tagged...

#### `aesop datasets get-aspect governed-tags`

Show governed tags this dataset is tagged with

**Usage**:

```console
$ aesop datasets get-aspect governed-tags [OPTIONS] DATASET_ID
```

**Arguments**:

* `DATASET_ID`: [required]

**Options**:

* `--output [TABULAR|CSV|JSON]`: The output format.Supported formats: [TABULAR, CSV, JSON]  [default: JSON]
* `--help`: Show this message and exit.

## `aesop documents`

Manages data documents on Metaphor.

**Usage**:

```console
$ aesop documents [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create`: Creates a data document.
* `delete`: Deletes a data document.

### `aesop documents create`

Creates a data document.

**Usage**:

```console
$ aesop documents create [OPTIONS] NAME CONTENT
```

**Arguments**:

* `NAME`: [required]
* `CONTENT`: [required]

**Options**:

* `--help`: Show this message and exit.

### `aesop documents delete`

Deletes a data document.

**Usage**:

```console
$ aesop documents delete [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

## `aesop domains`

Manages data domains in Metaphor.

**Usage**:

```console
$ aesop domains [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add`: Adds a data domain.
* `assets`: Manages assets in a Metaphor data domain.
* `get`: Gets a data domain defined in Metaphor.
* `list`: Lists data domains.
* `remove`: Removes a data domain.
* `saved-queries`: Manages saved live queries for Metaphor...

### `aesop domains add`

Adds a data domain.

**Usage**:

```console
$ aesop domains add [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `--description TEXT`
* `--tokenized-description TEXT`
* `--color TEXT`
* `--icon-key TEXT`
* `--parent-id TEXT`
* `--help`: Show this message and exit.

### `aesop domains assets`

Manages assets in a Metaphor data domain.

**Usage**:

```console
$ aesop domains assets [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add`: Adds an asset to a data domain.
* `get`: Gets the ids of the assets that belong to...
* `remove`: Removes an asset from the data domain.
* `remove-collection`: Removes a named asset collection from the...

#### `aesop domains assets add`

Adds an asset to a data domain.

**Usage**:

```console
$ aesop domains assets add [OPTIONS] DOMAIN_ID ASSET_ID
```

**Arguments**:

* `DOMAIN_ID`: [required]
* `ASSET_ID`: [required]

**Options**:

* `--collection-name TEXT`
* `--help`: Show this message and exit.

#### `aesop domains assets get`

Gets the ids of the assets that belong to the data domain.

**Usage**:

```console
$ aesop domains assets get [OPTIONS] DOMAIN_ID
```

**Arguments**:

* `DOMAIN_ID`: [required]

**Options**:

* `--help`: Show this message and exit.

#### `aesop domains assets remove`

Removes an asset from the data domain.

**Usage**:

```console
$ aesop domains assets remove [OPTIONS] DOMAIN_ID ASSET_ID
```

**Arguments**:

* `DOMAIN_ID`: [required]
* `ASSET_ID`: [required]

**Options**:

* `--collection-name TEXT`
* `--help`: Show this message and exit.

#### `aesop domains assets remove-collection`

Removes a named asset collection from the data domain.

**Usage**:

```console
$ aesop domains assets remove-collection [OPTIONS] DOMAIN_ID COLLECTION_NAME
```

**Arguments**:

* `DOMAIN_ID`: [required]
* `COLLECTION_NAME`: [required]

**Options**:

* `--help`: Show this message and exit.

### `aesop domains get`

Gets a data domain defined in Metaphor.

**Usage**:

```console
$ aesop domains get [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--output [TABULAR|CSV|JSON]`: The output format.Supported formats: [TABULAR, CSV, JSON]  [default: JSON]
* `--help`: Show this message and exit.

### `aesop domains list`

Lists data domains.

**Usage**:

```console
$ aesop domains list [OPTIONS]
```

**Options**:

* `--name TEXT`
* `--parent-id TEXT`
* `--help`: Show this message and exit.

### `aesop domains remove`

Removes a data domain.

**Usage**:

```console
$ aesop domains remove [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `aesop domains saved-queries`

Manages saved live queries for Metaphor data domains.

**Usage**:

```console
$ aesop domains saved-queries [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add`: Adds a live query to a Metaphor data domain.
* `remove`: Removes a saved live query from a Metaphor...

#### `aesop domains saved-queries add`

Adds a live query to a Metaphor data domain.

**Usage**:

```console
$ aesop domains saved-queries add [OPTIONS] DOMAIN_ID
```

**Arguments**:

* `DOMAIN_ID`: [required]

**Options**:

* `--search-context [DATA_DOCUMENT|DATA_GROUP|DBT_MODEL|Dashboards|Datasets|Groups|KnowledgeCards|LOOKER_EXPLORE|LOOKER_VIEW|Metrics|POWER_BI_DATASET|Persons|Pipelines|QUICK_SIGHT|TABLEAU_DATASOURCE|THOUGHT_SPOT_DATA_OBJECT]`
* `--facets-json TEXT`
* `--keyword TEXT`
* `--name TEXT`
* `--help`: Show this message and exit.

#### `aesop domains saved-queries remove`

Removes a saved live query from a Metaphor data domain.

**Usage**:

```console
$ aesop domains saved-queries remove [OPTIONS] DOMAIN_ID
```

**Arguments**:

* `DOMAIN_ID`: [required]

**Options**:

* `--saved-query-id TEXT`
* `--saved-query-name TEXT`
* `--help`: Show this message and exit.

## `aesop glossaries`

Manages glossary documents.

**Usage**:

```console
$ aesop glossaries [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `gen-template`: Generates a template of glossary CSV file...
* `import`: Imports a local business glossary file to...
* `schema`: Prints the expected schema for a glossary...

### `aesop glossaries gen-template`

Generates a template of glossary CSV file with some example values.

**Usage**:

```console
$ aesop glossaries gen-template [OPTIONS] [FILE]
```

**Arguments**:

* `[FILE]`: The file to write to.  [default: biz_glossary.csv]

**Options**:

* `--help`: Show this message and exit.

### `aesop glossaries import`

Imports a local business glossary file to Metaphor's data document storage. To see the schema or a simple template file, use `schema` or `gen-template` subcommands.

**Usage**:

```console
$ aesop glossaries import [OPTIONS] INPUT_FILE
```

**Arguments**:

* `INPUT_FILE`: The business glossary to import to Metaphor.  [required]

**Options**:

* `--directory TEXT`: The directory to import the file to. Should be in the format of a single slash-separated string. Any nonexisting subdirectory will be created.
* `--publish / --no-publish`: Whether to publish the imported file or not.  [default: publish]
* `--help`: Show this message and exit.

### `aesop glossaries schema`

Prints the expected schema for a glossary CSV file.

**Usage**:

```console
$ aesop glossaries schema [OPTIONS]
```

**Options**:

* `--output [TABULAR|CSV|JSON]`: The output format.Supported formats: [TABULAR, CSV, JSON]  [default: JSON]
* `--help`: Show this message and exit.

## `aesop help`

Print help for a command.

**Usage**:

```console
$ aesop help [OPTIONS] COMMAND:{tags}
```

**Arguments**:

* `COMMAND:{tags}`: [required]

**Options**:

* `--help`: Show this message and exit.

## `aesop info`

Display information about the Metaphor instance.

**Usage**:

```console
$ aesop info [OPTIONS]
```

**Options**:

* `--output [TABULAR|CSV|JSON]`: The output format. Supported formats: [TABULAR, CSV, JSON]  [default: TABULAR]
* `--help`: Show this message and exit.

## `aesop settings`

Manage settings in Metaphor.

**Usage**:

```console
$ aesop settings [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `custom-metadata`: Custom metadata settings
* `non-prod`: Non-prod settings
* `soft-deletion`: Soft deletion settings

### `aesop settings custom-metadata`

Custom metadata settings

**Usage**:

```console
$ aesop settings custom-metadata [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`
* `remove`: Removes the metadata config associated...
* `update`: Updates a config for a custom metadata.

#### `aesop settings custom-metadata get`

**Usage**:

```console
$ aesop settings custom-metadata get [OPTIONS]
```

**Options**:

* `--output [TABULAR|CSV|JSON]`: The output format.Supported formats: [TABULAR, CSV, JSON]  [default: JSON]
* `--help`: Show this message and exit.

#### `aesop settings custom-metadata remove`

Removes the metadata config associated with a key.

**Usage**:

```console
$ aesop settings custom-metadata remove [OPTIONS] KEY
```

**Arguments**:

* `KEY`: The key to remove custom metadata configs for.  [required]

**Options**:

* `--help`: Show this message and exit.

#### `aesop settings custom-metadata update`

Updates a config for a custom metadata. If no such config exists, it will be added.

**Usage**:

```console
$ aesop settings custom-metadata update [OPTIONS] [INPUT]
```

**Arguments**:

* `[INPUT]`: The input file to the command. Can either be piped in or passed as a command argument, otherwise an example input payload will be displayed onto the console, and the app will exit.  [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `--help`: Show this message and exit.

### `aesop settings non-prod`

Non-prod settings

**Usage**:

```console
$ aesop settings non-prod [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add`: Adds a non-prod dataset pattern.
* `get`: Gets the non-prod dataset patterns
* `remove`: Removes a non-prod dataset pattern.
* `set`: Batch updates all non-prod dataset patterns.

#### `aesop settings non-prod add`

Adds a non-prod dataset pattern.

**Usage**:

```console
$ aesop settings non-prod add [OPTIONS] DATABASE SCHEMA TABLE PLATFORM:{ATHENA|AZURE_BLOB_STORAGE|AZURE_DATA_LAKE_STORAGE|BIGQUERY|DOCUMENTDB|DYNAMODB|ELASTICSEARCH|EXTERNAL|GCS|GLUE|HIVE|HTTP|KAFKA|MONGODB|MSSQL|MYSQL|ORACLE|POSTGRESQL|RDS|REDIS|REDSHIFT|S3|SFTP|SNOWFLAKE|SYNAPSE|TRINO|UNITY_CATALOG|UNITY_CATALOG_VOLUME_FILE|UNKNOWN}
```

**Arguments**:

* `DATABASE`: [required]
* `SCHEMA`: [required]
* `TABLE`: [required]
* `PLATFORM:{ATHENA|AZURE_BLOB_STORAGE|AZURE_DATA_LAKE_STORAGE|BIGQUERY|DOCUMENTDB|DYNAMODB|ELASTICSEARCH|EXTERNAL|GCS|GLUE|HIVE|HTTP|KAFKA|MONGODB|MSSQL|MYSQL|ORACLE|POSTGRESQL|RDS|REDIS|REDSHIFT|S3|SFTP|SNOWFLAKE|SYNAPSE|TRINO|UNITY_CATALOG|UNITY_CATALOG_VOLUME_FILE|UNKNOWN}`: [required]

**Options**:

* `--account TEXT`
* `--is-case-sensitive / --no-is-case-sensitive`: [default: no-is-case-sensitive]
* `--help`: Show this message and exit.

#### `aesop settings non-prod get`

Gets the non-prod dataset patterns

**Usage**:

```console
$ aesop settings non-prod get [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

#### `aesop settings non-prod remove`

Removes a non-prod dataset pattern.

**Usage**:

```console
$ aesop settings non-prod remove [OPTIONS] DATABASE SCHEMA TABLE PLATFORM:{ATHENA|AZURE_BLOB_STORAGE|AZURE_DATA_LAKE_STORAGE|BIGQUERY|DOCUMENTDB|DYNAMODB|ELASTICSEARCH|EXTERNAL|GCS|GLUE|HIVE|HTTP|KAFKA|MONGODB|MSSQL|MYSQL|ORACLE|POSTGRESQL|RDS|REDIS|REDSHIFT|S3|SFTP|SNOWFLAKE|SYNAPSE|TRINO|UNITY_CATALOG|UNITY_CATALOG_VOLUME_FILE|UNKNOWN}
```

**Arguments**:

* `DATABASE`: [required]
* `SCHEMA`: [required]
* `TABLE`: [required]
* `PLATFORM:{ATHENA|AZURE_BLOB_STORAGE|AZURE_DATA_LAKE_STORAGE|BIGQUERY|DOCUMENTDB|DYNAMODB|ELASTICSEARCH|EXTERNAL|GCS|GLUE|HIVE|HTTP|KAFKA|MONGODB|MSSQL|MYSQL|ORACLE|POSTGRESQL|RDS|REDIS|REDSHIFT|S3|SFTP|SNOWFLAKE|SYNAPSE|TRINO|UNITY_CATALOG|UNITY_CATALOG_VOLUME_FILE|UNKNOWN}`: [required]

**Options**:

* `--account TEXT`
* `--is-case-sensitive / --no-is-case-sensitive`: [default: no-is-case-sensitive]
* `--help`: Show this message and exit.

#### `aesop settings non-prod set`

Batch updates all non-prod dataset patterns.

**Usage**:

```console
$ aesop settings non-prod set [OPTIONS] [INPUT]
```

**Arguments**:

* `[INPUT]`: The input file to the command. Can either be piped in or passed as a command argument, otherwise an example input payload will be displayed onto the console, and the app will exit.  [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `--help`: Show this message and exit.

### `aesop settings soft-deletion`

Soft deletion settings

**Usage**:

```console
$ aesop settings soft-deletion [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`
* `set`

#### `aesop settings soft-deletion get`

**Usage**:

```console
$ aesop settings soft-deletion get [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

#### `aesop settings soft-deletion set`

**Usage**:

```console
$ aesop settings soft-deletion set [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `enabled`
* `threshold_hours`

##### `aesop settings soft-deletion set enabled`

**Usage**:

```console
$ aesop settings soft-deletion set enabled [OPTIONS] ENABLED
```

**Arguments**:

* `ENABLED`: [required]

**Options**:

* `--help`: Show this message and exit.

##### `aesop settings soft-deletion set threshold_hours`

**Usage**:

```console
$ aesop settings soft-deletion set threshold_hours [OPTIONS] HOURS
```

**Arguments**:

* `HOURS`: [required]

**Options**:

* `--help`: Show this message and exit.

## `aesop tags`

Manage tags in Metaphor.

**Usage**:

```console
$ aesop tags [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add`: Add a single governed tag with optional...
* `add-value`: Add a value for a Metaphor governed tag...
* `assign`: Assign a governed tag to an asset.
* `batch-add`: Batch add governed tags with optional...
* `batch-assign`: Batch assign governed tags to multiple assets
* `batch-remove`: Batch remove governed tags from Metaphor.
* `batch-unassign`: Unassign governed tags from assets.
* `get`: Get governed tag
* `get-values`: Get the values of a governed tag
* `list`: List governed tags.
* `remove`: Remove a governed tag from Metaphor.
* `remove-value`: Remove a value of a governed tag from...
* `unassign`: Unassign a governed tag from an asset.

### `aesop tags add`

Add a single governed tag with optional description text to Metaphor.

**Usage**:

```console
$ aesop tags add [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `--description TEXT`
* `--color TEXT`
* `--icon-key TEXT`
* `--output [TABULAR|CSV|JSON]`: The output format.Supported formats: [TABULAR, CSV, JSON]  [default: JSON]
* `--help`: Show this message and exit.

### `aesop tags add-value`

Add a value for a Metaphor governed tag with optional description text.

**Usage**:

```console
$ aesop tags add-value [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `--description TEXT`
* `--tag-id TEXT`
* `--color TEXT`
* `--icon-key TEXT`
* `--output [TABULAR|CSV|JSON]`: The output format.Supported formats: [TABULAR, CSV, JSON]  [default: JSON]
* `--help`: Show this message and exit.

### `aesop tags assign`

Assign a governed tag to an asset.

**Usage**:

```console
$ aesop tags assign [OPTIONS] TAG_ID ASSET_ID
```

**Arguments**:

* `TAG_ID`: [required]
* `ASSET_ID`: [required]

**Options**:

* `--help`: Show this message and exit.

### `aesop tags batch-add`

Batch add governed tags with optional description text to Metaphor.

**Usage**:

```console
$ aesop tags batch-add [OPTIONS] [INPUT_FILE]
```

**Arguments**:

* `[INPUT_FILE]`: The input file to the command. Can either be piped in or passed as a command argument, otherwise an example input payload will be displayed onto the console, and the app will exit.  [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `--output [TABULAR|CSV|JSON]`: The output format.Supported formats: [TABULAR, CSV, JSON]  [default: JSON]
* `--help`: Show this message and exit.

### `aesop tags batch-assign`

Batch assign governed tags to multiple assets

**Usage**:

```console
$ aesop tags batch-assign [OPTIONS] [INPUT_FILE]
```

**Arguments**:

* `[INPUT_FILE]`: The input file to the command. Can either be piped in or passed as a command argument, otherwise an example input payload will be displayed onto the console, and the app will exit.  [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `--help`: Show this message and exit.

### `aesop tags batch-remove`

Batch remove governed tags from Metaphor.

**Usage**:

```console
$ aesop tags batch-remove [OPTIONS] [INPUT_FILE]
```

**Arguments**:

* `[INPUT_FILE]`: The input file to the command. Can either be piped in or passed as a command argument, otherwise an example input payload will be displayed onto the console, and the app will exit.  [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `--output [TABULAR|CSV|JSON]`: The output format.Supported formats: [TABULAR, CSV, JSON]  [default: JSON]
* `--help`: Show this message and exit.

### `aesop tags batch-unassign`

Unassign governed tags from assets.

**Usage**:

```console
$ aesop tags batch-unassign [OPTIONS] [INPUT_FILE]
```

**Arguments**:

* `[INPUT_FILE]`: The input file to the command. Can either be piped in or passed as a command argument, otherwise an example input payload will be displayed onto the console, and the app will exit.  [default: <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>]

**Options**:

* `--help`: Show this message and exit.

### `aesop tags get`

Get governed tag

**Usage**:

```console
$ aesop tags get [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--output [TABULAR|CSV|JSON]`: The output format.Supported formats: [TABULAR, CSV, JSON]  [default: JSON]
* `--help`: Show this message and exit.

### `aesop tags get-values`

Get the values of a governed tag

**Usage**:

```console
$ aesop tags get-values [OPTIONS] ID
```

**Arguments**:

* `ID`: [required]

**Options**:

* `--output [TABULAR|CSV|JSON]`: The output format.Supported formats: [TABULAR, CSV, JSON]  [default: JSON]
* `--help`: Show this message and exit.

### `aesop tags list`

List governed tags.

**Usage**:

```console
$ aesop tags list [OPTIONS]
```

**Options**:

* `--name TEXT`: Filter for the name of the governed tag
* `--output [TABULAR|CSV|JSON]`: The output format.Supported formats: [TABULAR, CSV, JSON]  [default: JSON]
* `--help`: Show this message and exit.

### `aesop tags remove`

Remove a governed tag from Metaphor.

**Usage**:

```console
$ aesop tags remove [OPTIONS] TAG_ID
```

**Arguments**:

* `TAG_ID`: [required]

**Options**:

* `--output [TABULAR|CSV|JSON]`: The output format.Supported formats: [TABULAR, CSV, JSON]  [default: JSON]
* `--help`: Show this message and exit.

### `aesop tags remove-value`

Remove a value of a governed tag from Metaphor.

**Usage**:

```console
$ aesop tags remove-value [OPTIONS] TAG_VALUE_ID
```

**Arguments**:

* `TAG_VALUE_ID`: [required]

**Options**:

* `--output [TABULAR|CSV|JSON]`: The output format.Supported formats: [TABULAR, CSV, JSON]  [default: JSON]
* `--help`: Show this message and exit.

### `aesop tags unassign`

Unassign a governed tag from an asset.

**Usage**:

```console
$ aesop tags unassign [OPTIONS] TAG_ID ASSET_ID
```

**Arguments**:

* `TAG_ID`: [required]
* `ASSET_ID`: [required]

**Options**:

* `--help`: Show this message and exit.

## `aesop upload`

Upload data assets from a CSV file.

**Usage**:

```console
$ aesop upload [OPTIONS] CSV_PATH
```

**Arguments**:

* `CSV_PATH`: Path to the CSV file containing data asset information  [required]

**Options**:

* `--help`: Show this message and exit.

## `aesop version`

Print Aesop's version.

**Usage**:

```console
$ aesop version [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `aesop webhooks`

Manages webhooks.

**Usage**:

```console
$ aesop webhooks [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Gets a list of webhooks that are...
* `get-payload-schema`: Gets the payload of a webhook trigger type.
* `register`: Registers a webhook to Metaphor.
* `unregister`: Unregisters a webhook from Metaphor.

### `aesop webhooks get`

Gets a list of webhooks that are registered to Metaphor.

**Usage**:

```console
$ aesop webhooks get [OPTIONS] [TRIGGER]:[DATASET_SCHEMA_CHANGED|SERVICE_REQUEST_CREATED|UNKNOWN]
```

**Arguments**:

* `[TRIGGER]:[DATASET_SCHEMA_CHANGED|SERVICE_REQUEST_CREATED|UNKNOWN]`

**Options**:

* `--help`: Show this message and exit.

### `aesop webhooks get-payload-schema`

Gets the payload of a webhook trigger type.

**Usage**:

```console
$ aesop webhooks get-payload-schema [OPTIONS] TRIGGER:{DATASET_SCHEMA_CHANGED|SERVICE_REQUEST_CREATED|UNKNOWN}
```

**Arguments**:

* `TRIGGER:{DATASET_SCHEMA_CHANGED|SERVICE_REQUEST_CREATED|UNKNOWN}`: The trigger type.  [required]

**Options**:

* `--help`: Show this message and exit.

### `aesop webhooks register`

Registers a webhook to Metaphor.

**Usage**:

```console
$ aesop webhooks register [OPTIONS] TRIGGER:{DATASET_SCHEMA_CHANGED|SERVICE_REQUEST_CREATED|UNKNOWN} [URL]
```

**Arguments**:

* `TRIGGER:{DATASET_SCHEMA_CHANGED|SERVICE_REQUEST_CREATED|UNKNOWN}`: The wewbhook trigger type.  [required]
* `[URL]`: [default: The url for the webhook. Metaphor will send a POST request to this URL.]

**Options**:

* `--help`: Show this message and exit.

### `aesop webhooks unregister`

Unregisters a webhook from Metaphor.

**Usage**:

```console
$ aesop webhooks unregister [OPTIONS] [WEBHOOK_ID]
```

**Arguments**:

* `[WEBHOOK_ID]`: [default: The ID of the webhook to unregister.]

**Options**:

* `--help`: Show this message and exit.

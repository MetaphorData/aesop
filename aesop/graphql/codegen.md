# Generate GraphQL client code

## Requirements

- Python >= 3.9
- `ariadne-codegen`

## Usage

Copy `@www/data/schema.gql` to this directory, and then run `./codegen.sh`.

## Existing files

### `codegen.sh`

Run this script to get the schema from DBT's Apollo server, and generate the corresponding GraphQL client code.

### `ariadne-codegen.toml`

Controls the behavior of `ariadne-codegen`.

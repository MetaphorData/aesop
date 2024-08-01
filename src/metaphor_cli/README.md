# Metaphor CLI - Source Code

This directory contains the source code for the Metaphor CLI tool. 

## File Structure

* **`cli.py`:**
    * Main entry point for the CLI application.
    * Defines the Typer application, commands, and subcommands.
    * Handles user interaction, input validation, and orchestrates data asset uploads.
* **`config.py`:**
    * Defines a `Config` class to manage configuration settings.
    * Stores the API key, upload domain, and other relevant parameters.
* **`data_asset_loaders.py`:**
    * Contains functions to load data asset information from CSV files.
    * Parses CSV data and converts it into a nested dictionary structure suitable for the Metaphor API.
* **`data_asset_uploaders.py`:**
    * Contains functions to upload different types of data assets.
    * Uses the `aiohttp` library to send asynchronous HTTP requests to the Metaphor API.
    * Constructs and executes GraphQL mutations for data asset creation.
* **`input_validation.py`:**
    * Provides functions for validating user inputs and data asset structures.
    * Ensures data integrity and prevents invalid data from being sent to the Metaphor API.
* **`__init__.py`:**
    * An empty file indicating that this directory is a Python package.

## Usage

Refer to the main [README.md](../../README.md) file in the root directory for instructions on setting up and using the Metaphor CLI tool.
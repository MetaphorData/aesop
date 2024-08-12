# Metaphor CLI Tool

This repository contains a command-line interface (CLI) tool designed for easy interaction with the Metaphor Data platform. The tool currently supports uploading data assets to your Metaphor Data instance.

## Features

* **Data Asset Uploads:** Upload data assets (knowledge cards) from a structured CSV file.

## Getting Started
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MetaphorData/aesop
   cd aesop
   ```

2. **Install Dependencies:**
   ```bash
    pip install -e .
    ```

3. **Get GraphQL schema:**
    ```
    please paste the schema in the schema.gql file in the aesop directory.
    ```
<<<<<<< HEAD
4. **Run the CLI Tool:**
    ```bash
    aesop --help
    ```

## Upading Schema

1. **Get GraphQL schema:**
    ```
    please paste the schema in the schema.gql file in the aesop directory, ensure it is named schema.gql.
    ```

2. **Run Ariadne Codegen:**
    ```bash
    ./generate_models.sh
    ```
=======

3. **Run the CLI Tool:**
    ```bash
    metaphor-cli
    ```
>>>>>>> 3020075eae2fdeb2bc7abda62d987a6d662b74a7

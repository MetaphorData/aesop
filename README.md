# Aesop, the Metaphor CLI Tool

This repository contains a command-line interface (CLI) tool designed for easy interaction with the Metaphor Data platform. The tool currently supports uploading data assets to your Metaphor Data instance.

## Commands

- **Info**: Display information about Metaphor.
- **Settings**: Manage settings in Metaphor.
- **Tags**: Manage tags in Metaphor.
- **Data Asset Uploads**: Upload data assets (knowledge cards) from a structured CSV file.

## Config file

The config file should include the following fields:

```yaml
domain: <DOMAIN> # Domain of the Metaphor instance. For `https://acme.metaphor.io`, use `acme` here.
api_key: <API_KEY>
```

By default, `aesop` will look for `~/.config/aesop.yml`. You can provide a path to your config file via option `--config-file`.

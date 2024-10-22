# Aesop, the Metaphor CLI Tool

This repository contains a command-line interface (CLI) tool designed for easy interaction with the Metaphor Data platform.

## Config file

The config file should include the following fields:

```yaml
environment: <ENVIRONMENT> # The prefix for the Metaphor app. E.g. for `https://acme.metaphor.io`, use `acme`.
api_key: <API_KEY>
```

By default, `aesop` will look for `~/.config/aesop.yml`. You can provide a path to your config file via option `--config-file`.

# Aesop, the Metaphor CLI Tool

This repository contains a command-line interface (CLI) tool designed for easy interaction with the Metaphor Data platform.

## Config file

The config file should include the following fields:

```yaml
url: <URL> # The Metaphor app's URL. E.g. `https://acme.metaphor.io`.
api_key: <API_KEY> # The api key.
```

By default, `aesop` will look for `~/.config/aesop.yml`. You can provide a path to your config file via option `--config-file`.

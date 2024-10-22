<a href="https://metaphor.io"><img src="https://github.com/MetaphorData/aesop/raw/main/logo.png" width="300" /></a>

# Aesop, the Metaphor CLI Tool

[![Codecov](https://img.shields.io/codecov/c/github/MetaphorData/aesop)](https://app.codecov.io/gh/MetaphorData/aesop/tree/main)
[![PyPI Version](https://img.shields.io/pypi/v/metaphor-aesop)](https://pypi.org/project/metaphor-aesop/)
![Python version 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)
![PyPI Downloads](https://img.shields.io/pypi/dm/metaphor-aesop)
[![License](https://img.shields.io/github/license/MetaphorData/aesop)](https://github.com/MetaphorData/aesop/blob/master/LICENSE)

This repository contains a command-line interface (CLI) tool designed for easy interaction with the Metaphor Data platform.

## Config file

The config file should include the following fields:

```yaml
url: <URL> # The Metaphor app's URL. E.g. `https://acme.metaphor.io`.
api_key: <API_KEY> # The api key.
```

By default, `aesop` will look for `~/.config/aesop.yml`. You can provide a path to your config file via option `--config-file`.

## Why Aesop?

[Aesop](https://en.wikipedia.org/wiki/Aesop) is arguably the greatest Metaphorist the world has ever known. His fables help many of us learn about the world around us, much like this CLI tool helps you interact with your metadata through Metaphor.

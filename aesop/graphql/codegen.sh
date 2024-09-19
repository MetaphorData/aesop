#!/usr/bin/env bash

poetry run ariadne-codegen --config ./ariadne-codegen.toml

# ariadne codegen generates async client even though we tell it to generate sync client
# It's easier to sed it to sync than trying to modify it...
#
# sed is not portable, these commands do not work if you're not on MacOSX.
sed -i '' -e 's/await //' generated/client.py
sed -i '' -e 's/async //' generated/client.py
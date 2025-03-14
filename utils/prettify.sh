#!/bin/bash
cd /app/
# Lint and Autoformat the code in place
# Remove unused imports
python -m autoflake --in-place --ignore-init-module-imports -r ./pixelator
# Perform all other steps
black --config pyproject.toml ./pixelator
black --config pyproject.toml ./test

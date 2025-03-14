#!/bin/bash
cd /app/

# Make a temp init.py that only has the content below the __README_CONTENT_IS_COPIED_ABOVE__ line
cp README.md pixelator/__init__.py
sed -i '1s/^/\"\"\"\n/' pixelator/__init__.py
echo "\"\"\"" >> pixelator/__init__.py
echo "from .pixelator import Pixelator" >> pixelator/__init__.py


# Specify versions for documentation purposes
VERSION="1.3.0"
OLD_DOC_VERSIONS="1.2.0 1.1.0 1.0.0 0.1"
export version_options="$VERSION $OLD_DOC_VERSIONS"

# generate the docs for a version function:
function generate_docs() {
    INPUT_VERSION=$1
    if [ $INPUT_VERSION != "./" ]; then
        if [ $INPUT_VERSION != $VERSION ]; then
            pip install "./dist/pixelator-$INPUT_VERSION.tar.gz"
        fi
    fi
    pdoc -o ./docs/$INPUT_VERSION -t ./doc_template pixelator
}

# Generate the docs for the current version
generate_docs ./
generate_docs $VERSION

# Generate the docs for all the old versions
for version in $OLD_DOC_VERSIONS; do
    generate_docs $version
done;

# Reinstall the current package as an egg
pip install -e .

docker build . --tag "pixelator" --quiet
docker run -it --rm \
    --volume "$(pwd):/app" \
    "pixelator"


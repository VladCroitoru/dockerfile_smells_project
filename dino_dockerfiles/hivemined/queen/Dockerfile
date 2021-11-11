FROM debian:8
MAINTAINER "Ryan - faceless.saint@gmail.com"

# label for use with Hivemined
LABEL hivemined.queen

# Copy run scripts
COPY ["src", "/usr/local/bin/"]

# Copy source directories for child images
COPY ["images", "/usr/local/src/"]

ENTRYPOINT ["/usr/local/bin/main.py"]

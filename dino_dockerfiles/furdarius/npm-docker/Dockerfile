# Npm Docker Container
# Base Dockerfile: node/node:slim
FROM node:slim

MAINTAINER furdarius <getlag@yandex.com>

# Updating npm:
RUN curl -sL https://npmjs.org/install.sh | sh && \
    npm --version

# Packages
RUN apt-get update && apt-get install -y \
        git \
    && rm -rf /var/lib/apt/lists/*

# Set up the application directory
VOLUME ["/app"]
WORKDIR /app

# Define default command.
ENTRYPOINT ["npm"]
CMD ["install"]

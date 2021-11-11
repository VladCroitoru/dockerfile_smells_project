# Gulp Docker Container
# Base Dockerfile: furdarius/npm-docker
FROM furdarius/npm-docker

MAINTAINER furdarius <getlag@yandex.com>

# Install webpack:
RUN npm install webpack -g

# Set up the application directory
VOLUME ["/app"]
WORKDIR /app

# Define default command.
ENTRYPOINT ["webpack"]
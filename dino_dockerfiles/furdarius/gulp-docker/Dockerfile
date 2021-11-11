# Gulp Docker Container
# Base Dockerfile: furdarius/npm-docker
FROM furdarius/npm-docker

MAINTAINER furdarius <getlag@yandex.com>

# Packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    libnotify-bin

# Install gulp:
RUN npm install --global gulp-cli

# Set up the application directory
VOLUME ["/app"]
WORKDIR /app

# Define default command.
ENTRYPOINT ["gulp"]
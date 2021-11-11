#
# Ghost Dockerfile
#
# https://github.com/dockerfile/ghost
#

# Pull base image.
FROM node:0.10

ENV GHOST_VERSION 0.5.7

# Install Ghost
RUN \
  apt-get update && \
  apt-get install -y unzip && \
  cd /tmp && \
  wget https://ghost.org/zip/ghost-$GHOST_VERSION.zip && \
  unzip ghost-$GHOST_VERSION.zip -d /ghost && \
  rm -f ghost-$GHOST_VERSION.zip && \
  cd /ghost && \
  npm install --production && \
  sed 's/127.0.0.1/0.0.0.0/' /ghost/config.example.js > /ghost/config.js && \
  useradd ghost --home /ghost

# Add files.
ADD start.bash /ghost-start

# Set environment variables.
ENV NODE_ENV production

# Define mountable directories.
VOLUME ["/data", "/ghost-override"]

# Define working directory.
WORKDIR /ghost

# Define default command.
CMD ["bash", "/ghost-start"]

# Expose ports.
EXPOSE 2368

FROM iojs:slim

MAINTAINER Mars Hsu <marshsu@gmail.com>

RUN apt-get update && \
    apt-get install -y git

RUN npm install -g sails grunt bower pm2 npm-check-updates
RUN mkdir /server

# Define mountable directories.
VOLUME ["/server"]

# Define working directory.
WORKDIR /server

# Expose ports.
EXPOSE 1337

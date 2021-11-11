# -------------------------------------------------------------------
#                               BASE NODE
# -------------------------------------------------------------------
# We need full node as we need git to download from some GitHub repos.
# -------------------------------------------------------------------
FROM node:8.12.0@sha256:06c7033a274aab131b07e7b8da8d1f823ee752a6e1e2bd46c0b459921ab2c39a as BASE
MAINTAINER Stefan Walther <swr-nixda@gmail.com>

ARG BASE_VERSION="0.1.1"

WORKDIR /opt/qix-info

RUN npm install qix-info@$BASE_VERSION -g

## -------------------------------------------------------------------
##                                RELEASE
## -------------------------------------------------------------------
FROM node:8.12.0-alpine@sha256:d75742c5fd41261113ed4706f961a21238db84648c825a5126ada373c361f46e as RELEASE

RUN apk update
RUN apk add bash

# Enables colored output
ENV FORCE_COLOR=true

WORKDIR /opt/qix-info

# OK, here we have to copy the symbolic link
# use npm config get prefix to get the node.js prefix https://stackoverflow.com/questions/18383476/how-to-get-the-npm-global-path-prefix

# Create the symbolic link
RUN ln -s /usr/local/lib/node_modules/qix-info/bin/cli.js /usr/local/bin/qix-info

# Copy the global packages previously being installed
COPY --from=BASE /usr/local/lib/node_modules /usr/local/lib/node_modules

COPY ./docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

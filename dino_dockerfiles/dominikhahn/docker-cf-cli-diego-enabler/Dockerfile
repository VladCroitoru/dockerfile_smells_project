# Pull base image.
FROM alpine:latest

MAINTAINER Dominik Hahn <dominik@monostream.com>

# Define working directory.
WORKDIR /workspace

# Set GOPATH variable
ENV GOPATH=/usr/local/bin
ENV CF_DIAL_TIMEOUT=60

# Install openssl and build dependencies
RUN apk --update add --quiet --no-cache openssl go zip && \
    apk --update add --quiet --no-cache --virtual build-dependencies git

# Install cf cli
RUN wget -O - "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar -C /usr/local/bin -zxf -

# Install Diego-Enabler, Antifreeze and autopilot
RUN cf install-plugin Diego-Enabler -f -r CF-Community

# Removing build dependencies
RUN apk del build-dependencies && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["/bin/ash"]

# Alpine Linux + Python 3 Web Application base image
# Based on the base image `alpine` (https://registry.hub.docker.com/_/alpine/)

# Pull base image
FROM alpine

# Install python3, bash, git, and common libs needed for web applications
RUN apk --update add python3 bash libevent-dev libffi-dev openssl-dev ca-certificates libxml2-dev libxslt-dev python3-dev build-base yaml git

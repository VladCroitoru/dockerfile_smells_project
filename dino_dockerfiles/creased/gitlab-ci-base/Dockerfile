#
# Docker generic base image for GitLab-CI
#
# Written by:
#   Baptiste MOINE <contact@bmoine.fr>
#

# Pull base image.
FROM docker:latest

MAINTAINER Baptiste MOINE <contact@bmoine.fr>

RUN apk update && \
    apk add --upgrade openssh-client python git python python-dev py-pip ca-certificates && \
    pip install --upgrade pip && \
    pip install --upgrade docker-compose

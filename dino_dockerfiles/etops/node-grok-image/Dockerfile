# This Dockerfile is intended to make a docker container out of a single Nectar toolbox job
FROM node:7.8.0
MAINTAINER dev@nectarfinancial.com

# Install all toolbox deps
RUN apt-get update
RUN apt-get -y install patch bison ctags flex gperf libevent-dev libpcre3-dev libtokyocabinet-dev poppler-utils

COPY . /

# Build grok
RUN make grok --directory /grok

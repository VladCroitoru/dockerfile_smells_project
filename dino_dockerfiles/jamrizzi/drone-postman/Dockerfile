############################################################
# Dockerfile to run postman-drone
# Based on Alpine
############################################################

FROM node:8.1-alpine

MAINTAINER Jam Risser (jamrizzi)

WORKDIR /app/

RUN apk add --no-cache \
        python \
        tini \
    && npm install -g \
        newman

COPY ./run.py /app/run.py

ENV PLUGIN_COLLECTION=""

ENTRYPOINT ["/sbin/tini", "--", "python", "/app/run.py"]

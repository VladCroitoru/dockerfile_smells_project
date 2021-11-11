# Copyright 2016, EMC, Inc.
ARG repo=node
ARG tag=8.11.1

FROM ${repo}:${tag}

COPY . /RackHD/on-core/

RUN cd /RackHD/on-core \
  && npm install --production

VOLUME /opt/monorail

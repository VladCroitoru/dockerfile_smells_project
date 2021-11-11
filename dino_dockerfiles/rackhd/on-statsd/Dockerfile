# Copyright 2016, EMC, Inc.

ARG repo=rackhd
ARG tag=devel

FROM ${repo}/on-core:${tag}

COPY . /RackHD/on-statsd/
WORKDIR /RackHD/on-statsd

COPY ./package.json /tmp/
RUN mkdir -p ./node_modules \
  && ln -s /RackHD/on-core ./node_modules/on-core \
  && ln -s /RackHD/on-core/node_modules/di ./node_modules/di \
  && npm install --ignore-scripts --production

EXPOSE 8125/udp
CMD [ "node", "/RackHD/on-statsd/index.js" ]

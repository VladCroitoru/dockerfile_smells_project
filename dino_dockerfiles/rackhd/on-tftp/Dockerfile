# Copyright 2016, EMC, Inc.

ARG repo=rackhd
ARG tag=devel

FROM ${repo}/on-core:${tag}

COPY . /RackHD/on-tftp/
WORKDIR /RackHD/on-tftp

RUN mkdir -p ./node_modules \
  && npm install --ignore-scripts --production \
  && rm -r ./node_modules/on-core ./node_modules/di \
  && ln -s /RackHD/on-core ./node_modules/on-core \
  && ln -s /RackHD/on-core/node_modules/di ./node_modules/di

EXPOSE 69/udp
VOLUME /RackHD/on-tftp/static/tftp
CMD [ "node", "/RackHD/on-tftp/index.js" ]

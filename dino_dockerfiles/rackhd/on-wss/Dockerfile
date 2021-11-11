# Copyright 2016, EMC, Inc.

ARG repo=rackhd
ARG tag=devel

FROM ${repo}/on-core:${tag}

COPY . /RackHD/on-wss/
WORKDIR /RackHD/on-wss

RUN mkdir -p ./node_modules \
  && ln -s /RackHD/on-core ./node_modules/on-core \
  && npm install --ignore-scripts --production

EXPOSE 9100
CMD [ "node", "/RackHD/on-wss/index.js" ]

FROM buildpack-deps:stretch
MAINTAINER Stipe Kotarac "stipe@kotarac.net"

RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends jq && \
  rm -rf /var/lib/apt/lists/*
RUN groupadd node && useradd -g node -s /bin/bash -d /node -m node
COPY . /buildpack
RUN make install -C /buildpack

WORKDIR /node/src
ONBUILD COPY . /node/src
ONBUILD RUN chown -R node:node /node/src
ONBUILD USER node
ONBUILD RUN buildpack-nodejs-build
ONBUILD ENV PATH /node/src/.buildpack-nodejs/node/bin:$PATH

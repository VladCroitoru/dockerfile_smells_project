FROM ubuntu:16.04

RUN groupadd --gid 1000 node \
  && useradd --uid 1000 --gid node --shell /bin/bash --create-home node

RUN apt-get -y update && apt-get install -y \
  curl \
  wget 

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 7.10.0

RUN curl -O https://nodejs.org/download/release/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
RUN curl -O https://nodejs.org/download/release/v${NODE_VERSION}/SHASUMS256.txt
RUN grep node-v${NODE_VERSION}-linux-x64.tar.gz SHASUMS256.txt | sha256sum -c -
RUN tar -xvf node-v${NODE_VERSION}-linux-x64.tar.gz --strip-components=1 -C /usr/local

RUN node -v
RUN npm -v

CMD [ "node" ]

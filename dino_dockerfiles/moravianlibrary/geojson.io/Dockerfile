FROM ubuntu:12.04.5

# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# install dependencies
RUN apt-get update -y && \
    apt-get install -y \
      build-essential \
      libssl-dev \
      python \
      git \
      curl \
      pkg-config \
      libcairo2-dev

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 0.10.40

# Install nvm with node and npm
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.26.1/install.sh | bash \
    && source $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/v$NODE_VERSION/bin:$PATH

RUN npm install geojson-extent
RUN npm install -g serve
RUN npm install -g jake
RUN npm install jshint

# build
RUN mkdir /build
COPY app /build
RUN cd /build && \
    npm link local_packages/github-api && \
    npm install && \
    make

COPY init.sh /init.sh

ENTRYPOINT /init.sh

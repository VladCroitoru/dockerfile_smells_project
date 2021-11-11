FROM ubuntu:16.04

ENV NVM_DIR="/usr/local/nvm" \
    NODE_VERSION=6.13.1 \
    APPLICATION_USER=pom \
    APPLICATION_HOME=/var/pom \
    BUILD_ARTIFACTS=/var/pom/.artifacts

RUN rm /bin/sh \
  && ln -s /bin/bash /bin/sh \
  && apt-get update -qq && apt-get install -y -q \
    apt-transport-https \
    curl \
    build-essential \
    git \
  && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && apt-get update -qq \
  && apt-get install -y -q \
   yarn \
  && curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.4/install.sh | bash \
  && . $NVM_DIR/nvm.sh \
  && nvm install $NODE_VERSION \
  && nvm alias default $NODE_VERSION \
  && nvm use default \
  && useradd -d $APPLICATION_HOME -u 1000 -m -s /bin/bash $APPLICATION_USER \

  && rm -rf /var/lib/apt/lists/*

RUN mkdir $BUILD_ARTIFACTS \
    && chown -R $APPLICATION_USER:$APPLICATION_USER $BUILD_ARTIFACTS

COPY scripts/ /usr/local/bin

VOLUME $BUILD_ARTIFACTS

ENV NODE_PATH=$NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules \
    PATH=$NVM_DIR/versions/node/v$NODE_VERSION/bin:./node_modules/.bin:$PATH

FROM maven:3-jdk-8
MAINTAINER Timoteo Ponce <timo.slack@gmail.com>

##########################
# INSTALL JAVA  and other deps
ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 7.2.0

USER root

RUN apt-get update && apt-get -y install curl  apt-transport-https && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    curl -sL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && \
    apt-get install -y git xvfb google-chrome-stable yarn && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN groupadd --gid 1000 node && \
    useradd --uid 1000 --gid node --shell /bin/bash --create-home node

RUN curl -kSLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" && \
    tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 && \
    rm "node-v$NODE_VERSION-linux-x64.tar.xz" && \
    ln -s /usr/local/bin/node /usr/local/bin/nodejs && \
    npm install -g bower gulp polymer-cli && npm cache clean


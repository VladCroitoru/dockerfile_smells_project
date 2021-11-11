FROM debian:jessie

ENV appDir /var/www/app/current
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 6.0.0
ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH
ENV AMQP_ADDRESS localhost

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update \
    && apt-get install -y -q --no-install-recommends \
    apt-transport-https \
    build-essential \
    ca-certificates \
    curl \
    g++ \
    gcc \
    git \
    make \
    nginx \
    sudo \
    wget \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -y autoclean
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.26.0/install.sh | bash \
    && source $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

RUN mkdir -p /var/www/app/current
WORKDIR ${appDir}

ADD package.json ./
RUN npm i && npm i -g pm2

ADD . /var/www/app/current

EXPOSE 4500

RUN cd /var/www/app/current && npm run build

CMD ["pm2", "start", "processes.json", "--no-daemon", "--node-args", "\"AMQP_ADDRESS=${AMQP_ADDRESS}\""]
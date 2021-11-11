FROM makeomatic/node:$NODE_VERSION

ENV NCONF_NAMESPACE=MS_USERS \
    NODE_ENV=$NODE_ENV

WORKDIR /src

COPY package.json yarn.lock ./
RUN \
  apk --update add --virtual .buildDeps \
    build-base \
    python3 \
    git \
    curl \
    openssl \
  && yarn --production --frozen-lockfile \
  && yarn cache clean \
  && apk del \
    .buildDeps \
    wget \
  && rm -rf \
    /tmp/* \
    /root/.node-gyp \
    /root/.npm \
    /etc/apk/cache/* \
    /var/cache/apk/*

COPY . /src
RUN  chown -R node /src
USER node

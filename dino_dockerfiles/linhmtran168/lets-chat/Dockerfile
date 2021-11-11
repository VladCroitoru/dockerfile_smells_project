FROM node:0.12-slim
MAINTAINER SD Elements

ENV BUILD_DEPS='g++ gcc git make python' \
    LCB_PLUGINS='lets-chat-ldap lets-chat-s3'

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


RUN set -x \
&&  apt-get update \
&&  apt-get install -y $BUILD_DEPS --no-install-recommends \
&&  rm -rf /var/lib/apt/lists/* \
&&  apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false $BUILD_DEPS

ENV PKG_JSON_URL=https://raw.githubusercontent.com/linhmtran168/lets-chat/master/package.json
ADD $PKG_JSON_URL ./package.json

RUN set -x \
&&  npm install --production \
&&  npm install $LCB_PLUGINS \
&&  npm dedupe \
&&  npm cache clean \
&&  rm -rf /tmp/npm*

ENV TAR_GZ_URL=https://github.com/linhmtran168/lets-chat/archive/master.tar.gz
ADD $TAR_GZ_URL ./master.tar.gz

RUN tar -xzvf master.tar.gz \
&&  cp -a lets-chat-master/. . \
&&  rm -rf lets-chat-master

RUN groupadd -r node \
&&  useradd -r -g node node \
&&  chown node:node uploads \
&&  mkdir -p builtAssets \
&&  chown node:node builtAssets

ENV LCB_DATABASE_URI=mongodb://mongo/letschat \
    LCB_HTTP_HOST=0.0.0.0 \
    LCB_HTTP_PORT=8080 \
    LCB_XMPP_ENABLE=true \
    LCB_XMPP_PORT=5222

USER node

EXPOSE 8080 5222

VOLUME ["/usr/src/app/config"]
VOLUME ["/usr/src/app/uploads"]

CMD ["npm", "start"]

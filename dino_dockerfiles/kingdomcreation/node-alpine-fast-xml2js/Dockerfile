FROM node:8.12-alpine

RUN apk add --no-cache --virtual .build-deps \
        binutils-gold \
        linux-headers \
        libgcc \
        gnupg \
        gcc \
        g++ \
        python \ 
        make \       
        curl \
    && npm install -g fast-xml2js --unsafe-perm \
    && cd ~ \
    && rm -rf .npm \
    && rm -rf .node-gyp \
    && rm -rf .gnupg \
    && rm -rf /tmp/* \
    && rm -rf /var/cache/apk/* \
    && npm cache clear --force \
    && apk del .build-deps \
    && cd /usr/local/lib/node_modules/fast-xml2js \
    && rm binding.gyp \
    && rm fast-xml2js.cpp \
    && rm -rf rapidxml \
    && rm -rf build
    
ENV NODE_PATH=/usr/local/lib/node_modules
###Match AWS Lambda Node Version
FROM node:12-alpine

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENTRYPOINT ["/bin/sh", "-l"]

###Update packages###
RUN echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
    && echo "@edgecommunity http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && apk update \
    && apk add --upgrade apk-tools@edge \
    && apk update \
    && apk upgrade \
    && npm install npm@latest -g \
###Install new packages###
#Parallel
    && apk add --no-cache parallel \
    && /usr/bin/env_parallel.sh --install \
    && echo '. `which env_parallel.sh`' >> /etc/profile \
#Libintl
    && apk add --no-cache libintl \
#Temp add gcc and tools
    && apk add gcc python3-dev libc6-compat linux-headers build-base cmake make musl-dev gettext-dev zip \
#Compiled Binaries
    && wget https://github.com/rilian-la-te/musl-locales/archive/master.zip \
    && unzip master.zip && cd musl-locales-master \
    && cmake . && make && make install \
    && cd .. \
    && rm master.zip && rm -Rf musl-locales-master \
#AWS cli
    && apk add python3 \
    && pip3 --no-cache-dir install --upgrade pip setuptools \
    && pip3 --no-cache-dir install awscli && aws configure set default.region us-west-2 && aws configure set default.s3.max_concurrent_requests 50 \
#AWS sam-local
    && pip3 --no-cache-dir install aws-sam-cli \
#Global NPM packages
    && yarn global add eslint eslint-config-standard eslint-plugin-import eslint-plugin-node eslint-plugin-promise eslint-plugin-standard eslint-plugin-react babel-eslint eslint-plugin-babel \
    && yarn global add lerna \
    && yarn global add jest \
#Portable Binaries
    && wget -O /usr/local/bin/yq "https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64" && chmod +x /usr/local/bin/yq \
###Clean Up
#Remove temp packages
    && apk del gcc python3-dev libc6-compat linux-headers build-base cmake make musl-dev gettext-dev zip \
#Clean caches
    && npm cache clean --force \
    && yarn cache clean \
    && rm /var/cache/apk/* \
###Verify
    && aws --version \
    && sam --version \
    && node --version \
    && npm --version \
    && yarn --version \
    && parallel --version \
    && yq --version \
    && locale

FROM mhart/alpine-node:4

MAINTAINER Jean-Charles Sisk <jeancharles@paypal.com>

ENV KAPPA_VERSION 1.0.0-rc.14
ENV GOOD_CONSOLE_VERSION ^2
ENV GOOD_VERSION ^3
ENV GOSU_VERSION 1.7
ENV TINI_VERSION 0.9.0

# create the user for kappa
RUN addgroup -S kappa && adduser -SDHG kappa kappa

RUN ARCH=$(ARCH=$(apk --print-arch); case $ARCH in x86_64)ARCH=amd64;; x86)ARCH=i386;; esac; echo $ARCH) && \
    apk add --update ca-certificates && \
    apk add --virtual=gpg gnupg && \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys \
    B42F6819007F00F88E364FD4036A9C25BF357DD4 0527A9B7 && \
    wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-${ARCH}" && \
    wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-${ARCH}.asc" && \
    wget -O /usr/local/bin/tini "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-static" && \
    wget -O /usr/local/bin/tini.asc "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-static.asc" && \
    gpg --verify-files /usr/local/bin/gosu.asc /usr/local/bin/tini.asc && \
    rm /usr/local/bin/gosu.asc /usr/local/bin/tini.asc && \
    chmod +x /usr/local/bin/gosu /usr/local/bin/tini && \
    apk del --purge gpg && \
    rm -rf $HOME/.gnupg /var/cache/apk/*

# install dependencies
RUN npm install -g kappa@$KAPPA_VERSION good@$GOOD_VERSION good-console@$GOOD_CONSOLE_VERSION \
    && npm cache clean \
    && mkdir -p /opt/kappa/

# add the config
COPY config.tmpl /opt/kappa/config.json
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

# Define mountable directories.
VOLUME ["/opt/kappa"]

# not EXPOSEing because port is defined in the config

WORKDIR /opt/kappa
ENTRYPOINT ["/entrypoint.sh"]

CMD ["kappa"]

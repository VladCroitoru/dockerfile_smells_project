FROM mhart/alpine-node:6.9

RUN set -ex \
    && apk add --no-cache \
        git \
        xvfb

ARG CYPRESS_VERSION
ARG CYPRESS_CLI_VERSION
ENV CYPRESS_VERSION=${CYPRESS_VERSION:-0.18.0} \
    CYPRESS_CLI_VERSION=${CYPRESS_CLI_VERSION:-0.12.0}

RUN set -ex \
    && npm i -g cypress-cli@${CYPRESS_CLI_VERSION} \
    && echo Cypress version to install $CYPRESS_VERSION \
    && cypress install \
    && cypress verify \
    && rm -rf /usr/share/man /tmp/* /var/tmp/* /root/.node-gyp

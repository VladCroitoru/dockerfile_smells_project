FROM alpine:3.12

MAINTAINER Dmitry Morgachev <izonder@gmail.com>

ENV S6_VERSION=v2.1.0.2 \
    NODE_VERSION=v14.15.4 \
    NODE_PREFIX=/usr \
    YARN_VERSION=v1.22.5 \
    YARN_PREFIX=/usr/share/yarn \
    YARN_BINARY=/usr/bin

RUN set -x \

##############################################################################
# Create source directory
##############################################################################

    && mkdir /src \

##############################################################################
# Install dependencies
##############################################################################

    && apk add --no-cache libstdc++ \
    && apk add --no-cache --virtual .build-deps \
        binutils-gold \
        curl \
        g++ \
        gcc \
        gnupg \
        linux-headers \
        make \
        python3 \

##############################################################################
# Install S6-overlay
##############################################################################

    && curl -o /tmp/s6-overlay-amd64.tar.gz -sSL https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz \
    && tar -zxf /tmp/s6-overlay-amd64.tar.gz -C / \

##############################################################################
# Install Nginx
##############################################################################

    && apk add --no-cache nginx \
    && rm -rf /etc/nginx/default.d \

##############################################################################
# Install Node
# Based on https://github.com/mhart/alpine-node/blob/master/Dockerfile (thank you)
# Note: we use ipv4.pool.sks-keyservers.net instead of ha.pool.sks-keyservers.net
# due to the issue: https://bugs.launchpad.net/ubuntu/+source/gnupg2/+bug/1625845
##############################################################################

    # gpg keys listed at https://github.com/nodejs/node#release-keys
    && for server in \
        ipv4.pool.sks-keyservers.net \
        keyserver.pgp.com \
        ha.pool.sks-keyservers.net \
    ; do \
        gpg --keyserver $server --recv-keys \
            4ED778F539E3634C779C87C6D7062848A1AB005C \
            94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
            74F12602B6F1C4E913FAA37AD3A89613643B6201 \
            71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
            8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600 \
            C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
            C82FA3AE1CBEDC6BE46B9360C43CEC45C17AB93C \
            DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
            A48C2BEE680E841632CD4E44F07496B3EB3C1762 \
            108F52B48DB57BB0CC439B2997B01419BD92F80A \
            B9AE9905FFD7803F25714661B63B535A4C206CA9 \
        && break; \
    done \

    # Download and validate the NodeJs source
    && mkdir /node_src \
    && cd /node_src \
    && curl -o node-${NODE_VERSION}.tar.gz -sSL https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.gz \
    && curl -o SHASUMS256.txt.asc -sSL https://nodejs.org/dist/${NODE_VERSION}/SHASUMS256.txt.asc \
    && gpg --verify SHASUMS256.txt.asc \
    && grep node-${NODE_VERSION}.tar.gz SHASUMS256.txt.asc | sha256sum -c - \

    # Compile and install
    && cd /node_src \
    && tar -zxf node-${NODE_VERSION}.tar.gz \
    && cd node-${NODE_VERSION} \
    && ./configure --prefix=${NODE_PREFIX} --without-npm \
    && make -j$(getconf _NPROCESSORS_ONLN) \
    && make install \

##############################################################################
# Install yarn
##############################################################################

    && for server in \
       ipv4.pool.sks-keyservers.net \
       keyserver.pgp.com \
       ha.pool.sks-keyservers.net \
   ; do \
       gpg --keyserver $server --recv-keys \
            6A010C5166006599AA17F08146C2130DFD2497F5 \
        && break; \
    done \

    # Download, validate and install the Yarn source
    && curl -o /tmp/yarn-${YARN_VERSION}.tar.gz -sSL https://github.com/yarnpkg/yarn/releases/download/${YARN_VERSION}/yarn-${YARN_VERSION}.tar.gz \
    && curl -o /tmp/yarn-${YARN_VERSION}.tar.gz.asc -sSL https://github.com/yarnpkg/yarn/releases/download/${YARN_VERSION}/yarn-${YARN_VERSION}.tar.gz.asc \
    && gpg --verify /tmp/yarn-${YARN_VERSION}.tar.gz.asc \
    && tar -zxf /tmp/yarn-${YARN_VERSION}.tar.gz -C /tmp \
    && mv -f /tmp/yarn-${YARN_VERSION} ${YARN_PREFIX} \
    && ln -sf ${YARN_PREFIX}/bin/yarn ${YARN_BINARY}/yarn \
    && ln -sf ${YARN_PREFIX}/bin/yarnpkg ${YARN_BINARY}/yarnpkg \

##############################################################################
# Clean up
##############################################################################

    && apk del .build-deps \
    && rm -rf \
        /node_src \
        /tmp/* \
        /var/cache/apk/* \
        /etc/nginx/conf.d/* \
        /usr/share/man

##############################################################################
# Configs and init scripts
##############################################################################

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./service/* /etc/services.d/*

EXPOSE 80 443 3000
ENTRYPOINT ["/init"]

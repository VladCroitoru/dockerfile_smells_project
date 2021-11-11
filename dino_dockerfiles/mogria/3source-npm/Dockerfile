FROM mogria/3source-base:latest

MAINTAINER "Mogria" <m0gr14@gmail.com>

COPY toolscript.sh /usr/bin/toolscript.sh
ENV NODE_VERSION 5.1.1

RUN apk add --update curl && \
    curl -sSL https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz > /root/node-v$NODE_VERSION.tar.gz && \
    apk add --update \
        g++ \
        gcc \
        git \
        linux-headers \
        make \
        python && \
    cd /root && \
    tar xzf node-v$NODE_VERSION.tar.gz && \
    rm node-v$NODE_VERSION.tar.gz && \
    cd node-v$NODE_VERSION && \
    ./configure && \
    make &&  \
    make install && \
    cd .. && \
    rm -r node-v$NODE_VERSION

RUN chmod +x /usr/bin/toolscript.sh && \
    git config --system url."https://github.com".insteadOf "git://github.com" && \
    npm install -g bower gulp

RUN mkdir -p /data/www
VOLUME ["/data"]

WORKDIR /data/www
ENTRYPOINT ["umask-wrapper.sh", "container-user.sh", "toolscript.sh"]

FROM alpine:latest

RUN apk add --no-cache libstdc++ perl \
    && apk add --no-cache \
               --virtual .build-dependencies \
               autoconf \
               automake \
               g++ \
               git \
               libtool \
               linux-headers \
               make \ 
               python2 \
               python2-dev \
               python3 \
               python3-dev \
    && git clone --single-branch \
                 --branch disable-line-numbers-flag \
                 https://github.com/inikolaev/pyflame.git \
    && cd /pyflame \
    && ./autogen.sh \
    && ./configure \
    && make \
    && make install \
    && cd / \
    && rm -rf /pyflame \
    && apk del .build-dependencies \
    && rm -f /var/cache/apk/*

RUN wget https://raw.githubusercontent.com/brendangregg/FlameGraph/master/flamegraph.pl \
    && chmod +x /flamegraph.pl \
    && mv /flamegraph.pl /usr/bin




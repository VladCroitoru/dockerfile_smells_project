FROM docker:17.09.0-ce

ARG compose_version=1.16.1

# Install docker-compose (extra complicated since the base image uses alpine as base)
RUN apk add --no-cache curl openssl ca-certificates \
    && curl -L https://github.com/docker/compose/releases/download/${compose_version}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    && wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub \
    && wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-2.23-r3.apk \
    && apk add --no-cache glibc-2.23-r3.apk && rm glibc-2.23-r3.apk \
    && ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ \
    && ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib

# This is necessary for running Elasticsearch containers: https://github.com/docker-library/elasticsearch/issues/111
RUN echo sysctl -w vm.max_map_count=262144

RUN docker-compose -v

FROM alpine:3.6

MAINTAINER Billy Ray Teves <billyteves@gmail.com>

ENV CASSANDRA_VERSION      cassandra-3.11.0
ENV PATH                   "$PATH:/opt/cassandra/bin"

RUN set -ex \
    && apk add --no-cache ca-certificates \
    && apk update --no-cache \
    && apk upgrade --no-cache \
    && apk add --no-cache --virtual .build-deps \

    # Install and delete apks as dependencies
    curl \
    unzip \

    # Cassandra
    && mkdir -p /opt/ \
    && curl -L https://github.com/apache/cassandra/archive/$CASSANDRA_VERSION.zip --output /tmp/cassandra.zip \
    && unzip /tmp/cassandra.zip -d /tmp/cassandra \
    && mv /tmp/cassandra/cassandra-$CASSANDRA_VERSION /opt/cassandra \
    && apk del .build-deps \

    && apk add --no-cache --virtual --update \
    python2 \
    openjdk8 \

    # Cleanup

    && rm -rf /var/cache/apk/* \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

ENTRYPOINT ["cqlsh"]

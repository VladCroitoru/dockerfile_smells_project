FROM alpine:3.6

ENV LANG C.UTF-8

RUN { \
        echo '#!/bin/sh'; \
        echo 'set -e'; \
        echo; \
        echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
    } > /usr/local/bin/docker-java-home \
    && chmod +x /usr/local/bin/docker-java-home

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin
ENV JAVA_VERSION 8u131
ENV JAVA_ALPINE_VERSION 8.131.11-r2

RUN set -x \
	&& apk add --no-cache \
		openjdk8="$JAVA_ALPINE_VERSION" \
	&& [ "$JAVA_HOME" = "$(docker-java-home)" ]

ENV DIGDAG_VERSION=0.9.21

RUN apk add --no-cache curl && \
    curl -o /usr/bin/digdag --create-dirs -L "https://dl.digdag.io/digdag-$DIGDAG_VERSION" && \
    chmod +x /usr/bin/digdag && \
    apk del curl && \
    adduser -h /var/lib/digdag -g 'digdag user' -s /sbin/nologin -D digdag && \
    mkdir -p /var/lib/digdag/logs/tasks /var/lib/digdag/logs/server && \
    chown -R digdag.digdag /var/lib/digdag && \
    apk --no-cache update && \
    apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    apk --no-cache add ca-certificates curl groff less tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata && \
    apk --no-cache add bash jq && \
    pip --no-cache-dir install --upgrade pip && \
    rm -rf /var/cache/apk/*

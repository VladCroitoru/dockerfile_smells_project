From alpine:3.5
MAINTAINER leafney "babycoolzx@126.com"

RUN echo "http://dl-4.alpinelinux.org/alpine/v3.5/main" >> /etc/apk/repositories && \
	echo "http://dl-4.alpinelinux.org/alpine/v3.5/community" >> /etc/apk/repositories

ENV ERLANG_PKG_VERSION=19.1.0-r0 \
    RABBITMQ_VERSION=3.6.6 \
    RABBITMQ_HOME=/rabbitmq

ENV PATH=${RABBITMQ_HOME}/sbin:$PATH

RUN apk add --update --no-cache curl tar xz && \
    apk add erlang=${ERLANG_PKG_VERSION} \
    erlang-mnesia=${ERLANG_PKG_VERSION} \
    erlang-public-key=${ERLANG_PKG_VERSION} \
    erlang-asn1=${ERLANG_PKG_VERSION} \
    erlang-hipe=${ERLANG_PKG_VERSION} \
    erlang-crypto=${ERLANG_PKG_VERSION} \
    erlang-eldap=${ERLANG_PKG_VERSION} \
    erlang-inets=${ERLANG_PKG_VERSION} \
    erlang-os-mon=${ERLANG_PKG_VERSION} \
    erlang-sasl=${ERLANG_PKG_VERSION} \
    erlang-ssl=${ERLANG_PKG_VERSION} \
    erlang-syntax-tools=${ERLANG_PKG_VERSION} \
    erlang-xmerl=${ERLANG_PKG_VERSION}

RUN mkdir -p ${RABBITMQ_HOME} && \
    curl -sSL https://www.rabbitmq.com/releases/rabbitmq-server/v${RABBITMQ_VERSION}/rabbitmq-server-generic-unix-${RABBITMQ_VERSION}.tar.xz | tar -xJo -C ${RABBITMQ_HOME} --strip-components 1 && \
    apk del --purge curl tar xz && \
    rm -rf /var/cache/apk/*

COPY ./docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
RUN chmod +x usr/local/bin/docker-entrypoint.sh

VOLUME ["${RABBITMQ_HOME}/var"]

EXPOSE 4369 5671 5672 15672 25672
CMD ["docker-entrypoint.sh"]
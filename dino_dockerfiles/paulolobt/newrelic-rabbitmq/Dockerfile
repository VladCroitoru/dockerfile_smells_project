FROM ruby:2.4-alpine

ENV RABBITMQ_PLUGIN_VERSION 1.0.5
ENV RABBITMQ_PLUGIN_URL https://github.com/paulolobt/newrelic_pivotal_agent/archive/pivotal_agent-${RABBITMQ_PLUGIN_VERSION}.tar.gz

RUN mkdir -p /app
WORKDIR /app

RUN set -x \
    && apk add --no-cache --virtual .build-deps \
        ca-certificates \
        gcc \
        make \
        musl-dev \
        openssl \
        tar \
    && wget -O rabbitmq-plugin.tar.gz "$RABBITMQ_PLUGIN_URL" \
    && tar -xzf rabbitmq-plugin.tar.gz -C /app --strip-components=1 \
    && bundle install \
    && rm rabbitmq-plugin.tar.gz \
    && apk del .build-deps

COPY config/newrelic_plugin.yml /app/config/newrelic_plugin.yml

CMD ["ruby", "pivotal_agent"]

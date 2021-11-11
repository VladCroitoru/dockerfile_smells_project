FROM fluent/fluentd:v0.12.29
MAINTAINER Waleed Samy <waleedsamy634@gmail.com>
WORKDIR /home/fluent
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH


USER root
RUN apk --no-cache --update add sudo build-base ruby-dev && \

    sudo -u fluent fluent-gem install fluent-plugin-elasticsearch fluent-plugin-record-reformer \
    fluent-plugin-flatten-hash:0.2.0 fluent-plugin-secure-forward fluent-plugin-parser \
    fluent-plugin-grok-parser:1.0.0 fluent-plugin-prometheus \
    fluent-plugin-rewrite-tag-filter fluent-plugin-grep fluent-plugin-slack && \
    rm -rf /home/fluent/.gem/ruby/2.3.0/cache/*.gem && sudo -u fluent gem sources -c && \
    apk del sudo build-base ruby-dev && rm -rf /var/cache/apk/*

# listen port 24224 for Fluentd forward protocol
EXPOSE 24224
# prometheus plugin expose metrics at 0.0.0.0:24231/metrics
EXPOSE 24231

USER fluent

COPY fluent.conf /fluentd/etc/
COPY plugins/json_in_string.rb /fluentd/plugins/

# to have the permission to access /var/lib/docker/containers and /var/log/containers
USER root
ENV ELASTICSEARCH_HOST elasticsearch
ENV ELASTICSEARCH_PORT 9200
ENV ELASTICSEARCH_INDEX logstash
ENV ELASTICSEARCH_USER ''
ENV ELASTICSEARCH_PASSWORD ''
ENV ELASTICSEARCH_SCHEMA http
ENV ELASTICSEARCH_SSL_VERIFY false

ENV SLACK_WEBHOOK_URL https://hooks.slack.com/services/XXX/XXX/XXX
ENV SLACK_CHANNEL general

ENV KIBANA_HOST http://kibana.internal.domain.com

CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins/ $FLUENTD_OPT

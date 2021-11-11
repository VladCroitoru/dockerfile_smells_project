FROM ruby:2.2.5-slim

MAINTAINER Wael <wael@rsnewmedia.com>

COPY .gemrc /root/

# Temporary pin google-protobuf to 3.0.0.alpha.4.0
# There are some concerns on the performance of the latest version
RUN apt-get update -y && apt-get install -yy \
      build-essential \
      zlib1g-dev \
      libjemalloc1 && \
    gem install fluentd:0.12.33 && \
    gem install google-protobuf -v 3.0.0.alpha.4.0 --pre && \
      fluent-gem install \
      fluent-plugin-ec2-metadata \
      fluent-plugin-hostname \
      fluent-plugin-retag \
      fluent-plugin-kinesis \
      fluent-plugin-elasticsearch \
      fluent-plugin-record-modifier \
      fluent-plugin-multi-format-parser \
      fluent-plugin-kinesis-aggregation \
      fluent-plugin-concat \
      fluent-plugin-parser \
      fluent-plugin-secure-forward \
      fluent-plugin-rewrite-tag-filter \
      fluent-plugin-record-reformer \
      fluent-plugin-systemd:0.0.8 \
      fluent-plugin-grok-parser \
      fluent-plugin-detect-exceptions \
      ffi \
      fluent-plugin-kubernetes_metadata_filter \
      fluent-plugin-statsd-event:0.1.1 && \
    apt-get purge -y build-essential && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /var/log/fluent

# Copy plugins
COPY plugins /fluentd/plugins/
COPY ./fluentd.conf /fluentd/etc/

ENV FLUENTD_CONF="fluentd.conf"
ENV FLUENTD_OPT=""

# port monitor forward debug
EXPOSE 24220   24224   24230

ENV LD_PRELOAD "/usr/lib/x86_64-linux-gnu/libjemalloc.so.1"
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins $FLUENTD_OPT
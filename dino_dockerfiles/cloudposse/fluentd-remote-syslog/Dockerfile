FROM fluent/fluentd:latest
MAINTAINER Erik Osterman <erik@cloudposse.com>

ENV PATH=/home/fluent/.gem/ruby/2.3.0/bin:$PATH

USER root

WORKDIR /home/fluent

# https://rubygems.org/gems/fluent-plugin-remote_syslog
# https://rubygems.org/gems/fluent-plugin-record-reformer
# https://rubygems.org/gems/fluent-plugin-kubernetes_metadata_filter

RUN apk --no-cache --update add sudo build-base ruby-dev && \
    sudo -u fluent gem install --no-document fluent-plugin-record-reformer -v 0.8.2 && \
    sudo -u fluent gem install --no-document fluent-plugin-kubernetes_metadata_filter -v 0.26.2 && \
    sudo -u fluent gem install --no-document fluent-plugin-remote_syslog -v 0.3.2 && \
    rm -rf /home/fluent/.gem/ruby/2.3.0/cache/*.gem && \
    sudo -u fluent gem sources -c && \
    apk del sudo build-base ruby-dev && \
    rm -rf /var/cache/apk/*

EXPOSE 24284

CMD exec fluentd -c /fluentd/etc/fluent.conf -p /fluentd/plugins $FLUENTD_OPT


FROM ruby:2.5.1

RUN apt-get update \
 && apt-get install gettext-base --yes \
 && apt-get clean all \
 && rm -rf /var/lib/apt/lists/* \
 && gem install fluentd \
 && fluent-gem install  \
  oj \
  fluent-mixin-config-placeholders \
  fluent-mixin-plaintextformatter \
  fluent-plugin-splunkhec:1.5 \
  fluent-plugin-kubernetes_metadata_filter:1.0.1 \
  fluent-plugin-rewrite-tag-filter

COPY docker-entrypoint /docker-entrypoint
COPY td-agent.conf.template /etc/td-agent/

# Run the Fluentd service.
ENTRYPOINT ["/docker-entrypoint"]

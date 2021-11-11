FROM fluent/fluentd:v1.1.1-debian

USER root
WORKDIR /home/fluent
ENV PATH /fluentd/vendor/bundle/ruby/2.3.0/bin:$PATH
ENV GEM_PATH /fluentd/vendor/bundle/ruby/2.3.0
ENV GEM_HOME /fluentd/vendor/bundle/ruby/2.3.0
# skip runtime bundler installation
ENV FLUENTD_DISABLE_BUNDLER_INJECTION 1

COPY Gemfile* /fluentd/

RUN buildDeps="make gcc g++ libc-dev ruby-dev libffi-dev" \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    $buildDeps libjemalloc1 ruby-bundler \
 && bundle config silence_root_warning true \
 && bundle install --gemfile=/fluentd/Gemfile --path=/fluentd/vendor/bundle \
 && SUDO_FORCE_REMOVE=yes \
   apt-get purge -y --auto-remove -o APT::AutoREmove::RecommendsImportant=false $buildDeps \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem

# Copy plugins
COPY plugins /fluentd/plugins/
COPY entrypoint.sh /fluentd/entrypoint.sh

# Environment variables
ENV FLUENTD_OPT=""
ENV FLUENTD_CONF="fluent.conf"

ENTRYPOINT ["/fluentd/entrypoint.sh"]

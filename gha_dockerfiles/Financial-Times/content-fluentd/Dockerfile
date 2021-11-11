FROM fluent/fluentd:v1.7-debian-1

USER root

ENV PATH /fluentd/vendor/bundle/ruby/2.6.0/bin:$PATH
ENV GEM_PATH /fluentd/vendor/bundle/ruby/2.6.0
ENV GEM_HOME /fluentd/vendor/bundle/ruby/2.6.0

COPY Gemfile* /fluentd/

RUN buildDeps="sudo make gcc g++ libc-dev ruby-dev libffi-dev" \
   && apt-get update \
   && apt-get upgrade -y \
   && apt-get install -y --no-install-recommends $buildDeps ruby-bundler \
   && gem update --system \
   && gem install bundler:2.0.2 \
   && bundle config silence_root_warning true \
   && bundle install --gemfile=/fluentd/Gemfile --path=/fluentd/vendor/bundle \
   && SUDO_FORCE_REMOVE=yes apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $buildDeps \
   && rm -rf /var/lib/apt/lists/* \
   && gem sources --clear-all \
   && rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem

COPY ./conf/* /fluentd/etc/

COPY entrypoint.sh /fluentd/entrypoint.sh

ENV FLUENTD_OPT=""
ENV FLUENTD_CONF="fluent.conf"

# Run Fluentd
CMD ["/fluentd/entrypoint.sh"]

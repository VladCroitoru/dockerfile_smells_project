FROM fluent/fluentd:debian-onbuild
MAINTAINER TAGOMORI Satoshi <tagomoris@gmail.com>
LABEL Description="Fluentd docker image" Vendor="Fluent Organization" Version="1.1"

# USER fluent
USER root
WORKDIR /home/fluent
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH

ENV LANGUAGE C.UTF-8
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV LC_CTYPE C.UTF-8

COPY Gemfile ./

RUN buildDeps="sudo make gcc g++ libc-dev ruby-dev git" \
 && apt-get update \
 && apt-get install -y --no-install-recommends $buildDeps \
 && apt-get install -y default-libmysqlclient-dev \
 && sudo -u fluent gem install \
  mysql2 \
  mysql-slowquery-parser \
  fluent-plugin-elasticsearch \
  fluent-plugin-rewrite \
 && gem install bundler \
 && sudo -u fluent git clone https://github.com/kenjiskywalker/fluent-plugin-rds-slowlog.git \
  && cd fluent-plugin-rds-slowlog \
  && bundle install \
  && sudo -u fluent rake build \
  && sudo -u fluent gem install pkg/fluent-plugin-rds-slowlog-0.0.7.gem \
 && sudo -u fluent gem sources --clear-all \
  && SUDO_FORCE_REMOVE=yes \
     apt-get purge -y --auto-remove \
                   -o APT::AutoRemove::RecommendsImportant=false \
                   $buildDeps \
  && rm -rf /var/lib/apt/lists/* \
            /home/fluent/.gem/ruby/2.3.0/cache/*.gem

# USER fluent

EXPOSE 24284
CMD fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins $FLUENTD_OPT

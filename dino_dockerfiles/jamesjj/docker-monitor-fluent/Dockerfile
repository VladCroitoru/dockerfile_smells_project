FROM alpine:3.7

LABEL owner_team=OPS

WORKDIR /opt/docker-monitor-fluent

COPY Gemfile ./

RUN \
  apk upgrade --no-cache  && \
  apk add --no-cache \
    ca-certificates \
    ruby \
    ruby-irb \
    ruby-dev \
    ruby-bundler \
    ruby-json \
    git \
    build-base \
  && bundle install --no-color --verbose \
  && apk del build-base git

RUN \
  mkdir /home/app_daemon \
  && adduser -h /home/app_daemon -s /sbin/nologin -D -g app_daemon app_daemon \
  && chown -R app_daemon:app_daemon /home/app_daemon

COPY *.rb ./

RUN \
  chown app_daemon:app_daemon /opt/docker-monitor-fluent/*.rb \
  && chmod a-w /opt/docker-monitor-fluent/*.rb

# Usually reliably reading the docker socket, needs root (or docker group), so not switching to non-root for now
# USER app_daemon

ARG APP_CONFIG_VERSION
ENV APP_CONFIG_VERSION ${APP_CONFIG_VERSION:-unknown}

CMD [ "/usr/bin/ruby", "--", "./docker-monitor-fluent.rb" ]


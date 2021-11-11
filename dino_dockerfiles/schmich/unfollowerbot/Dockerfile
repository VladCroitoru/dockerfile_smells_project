FROM alpine:3.4
MAINTAINER Chris Schmich <schmch@gmail.com>
RUN apk add --no-cache \
  tzdata \
  jq \
  ruby \
  ruby-rdoc \
  ruby-irb \
  ruby-io-console \
  ca-certificates
COPY start.sh /start.sh
RUN chmod +x /start.sh
RUN gem install bundler
COPY crontab /var/spool/cron/crontabs/root
COPY src /srv/unfollowerbot
WORKDIR /srv/unfollowerbot
RUN bundle install
ENTRYPOINT ["/start.sh"]

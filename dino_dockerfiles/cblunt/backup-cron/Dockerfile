FROM ruby:2.3-alpine

# Set timezone
RUN apk add --update tzdata && \
    cp /usr/share/zoneinfo/Europe/London /etc/localtime && \
    echo "Europe/London" > /etc/timezone

# Get the latest Postgres client
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories && \
    apk --update add "postgresql@edge<9.6" "postgresql-contrib@edge<9.6" ruby-dev tar

COPY Gemfile .
COPY Gemfile.lock .

# Install dependencies
RUN apk add openssl

# Install gems
RUN apk add --virtual build-dependencies build-base libxml2-dev libxslt-dev \
      &&  bundle config build.nokogiri --use-system-libraries \
      &&  bundle install --jobs=4

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh

RUN mkdir -p /root/Backup
WORKDIR /root/Backup

COPY config.rb .
COPY schedule.rb .

COPY models/default.rb /root/Backup/models/default.rb

VOLUME ["/root/Backup/models"]

CMD ["/docker-entrypoint.sh"]

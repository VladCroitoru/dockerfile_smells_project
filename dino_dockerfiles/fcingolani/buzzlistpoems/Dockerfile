FROM ruby:2.1

ENV CRON_SCRAP_SCHEDULE="* * * * *" \
    CRON_TWEET_SCHEDULE="* * * * *"

COPY docker-cmd.sh /usr/bin/

RUN apt-get update \
    && apt-get install -y wget cron \
    && wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && tar -xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && rm wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && mv wkhtmltox /opt/ \
    && ln -s /opt/wkhtmltox/bin/wkhtmltoimage /usr/bin/wkhtmltoimage \
    && chmod +x /usr/bin/docker-cmd.sh \
    && touch /var/log/cron.log \
    && mkdir -p /usr/src/app

WORKDIR /usr/src/app

# Had to disable this because bundler is failing to add support for "ruby"
# platform when running in windows -_-
# https://github.com/bundler/bundler/pull/5231
# RUN bundle config --global frozen 1
# COPY Gemfile.lock /usr/src/app/

COPY Gemfile /usr/src/app/

RUN bundle install

COPY . /usr/src/app

CMD ["docker-cmd.sh"]

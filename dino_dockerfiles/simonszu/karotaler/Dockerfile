FROM ruby:2.5-alpine

RUN apk --no-cache add \
    bash \
    build-base \
    gettext \
    tzdata

ENV TZ=Europe/Berlin

RUN gem install mechanize

RUN apk del build-base

RUN mkdir /template \
    && mkdir /app

COPY karotaler.rb /template
COPY crontab.txt /template
RUN /usr/bin/crontab /template/crontab.txt

COPY run.sh /

RUN chmod +x /run.sh \
    && touch /var/log/cron.log

ENTRYPOINT ["/run.sh"]

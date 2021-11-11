FROM ruby:alpine

RUN apk add --no-cache \
  alpine-sdk \
  nodejs \
  mariadb-dev \
  sqlite-dev \
  postgresql-dev

RUN gem install rails --no-ri --no-rdoc

WORKDIR /opt

ENTRYPOINT ["rails", "new"]

CMD ["-h"]

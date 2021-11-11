FROM ruby:2.3.5-alpine

ENV LC_ALL C.UTF-8

RUN apk add --update --upgrade \
  build-base \
  libxml2-dev \
  libxslt-dev \
  mysql-dev \
  nodejs \
  tzdata \
  netcat-openbsd \
  && rm -rf /var/cache/apk/*

# Use libxml2, libxslt a packages from alpine for building nokogiri
RUN bundle config build.nokogiri --use-system-libraries

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY Gemfile* /usr/src/app/
RUN bundle config --global jobs 8
RUN bundle install --system

COPY . /usr/src/app

EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]

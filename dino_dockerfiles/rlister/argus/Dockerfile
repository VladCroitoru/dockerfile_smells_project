FROM alpine:3.3

MAINTAINER rlister@gmail.com

RUN apk -U upgrade && \
    apk add -U bash build-base ca-certificates git openssh ruby ruby-dev ruby-io-console && \
    rm -rf /var/cache/apk/*

## ensure bundler is up to date
RUN gem install bundler -v '>= 1.9.1' --no-rdoc --no-ri

WORKDIR /app

## minimum required to bundle
ADD Gemfile* *.gemspec /app/
ADD lib/argus/version.rb /app/lib/argus/version.rb

RUN bundle install

ADD bin /app/bin
ADD lib /app/lib

ENV ARGUS_QUEUE argus

CMD ["bin/argus-worker"]
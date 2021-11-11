FROM ruby:2.3.1-alpine

MAINTAINER Kento Haneda <kento@haneda.me>

ENV BUILD_PACKAGES="ruby-dev build-base mysql-dev nodejs" \
    PACKAGES="libxml2-dev zlib-dev libxslt-dev tzdata" \
    RAILS_VERSION="4.2.6"

RUN \
  apk --update upgrade && \
  apk add $BUILD_PACKAGES $PACKAGES $DEV_PACKAGES && \
  
  # gem no document
  echo 'gem: --no-document' >> ~/.gemrc && \
  cp ~/.gemrc /etc/gemrc && \
  chmod uog+r /etc/gemrc  && \
  
  gem install nokogiri -- --use-system-libraries && \
  gem install rails --version "$RAILS_VERSION" && \
  
  # cleanup mysql 
  cp -L /usr/lib/libmysqlclient.so.18 ~/ && \
  apk del $BUILD_PACKAGES && \
  mv ~/libmysqlclient.so.18 /usr/lib && \
  
  find / -type f -iname \*.apk-new -delete && \
  rm -rf /var/cache/apk/* && \
  rm -rf /usr/lib/lib/ruby/gems/*/cache/* && \
  rm -rf ~/.gem

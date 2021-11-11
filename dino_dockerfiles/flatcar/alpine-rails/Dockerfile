FROM alpine:3.2

MAINTAINER Laura Frank <laura@codeship.com>

ENV BUILD_PACKAGES="curl-dev ruby-dev build-base" \
    DEV_PACKAGES="zlib-dev libxml2-dev libxslt-dev tzdata yaml-dev" \
    RUBY_PACKAGES="ruby ruby-io-console ruby-json yaml nodejs" \
    RAILS_VERSION="4.2.3"

RUN \
  apk --update --upgrade add $BUILD_PACKAGES $RUBY_PACKAGES $DEV_PACKAGES && \
  gem install -N bundler && \
  find / -type f -iname \*.apk-new -delete && \
  rm -rf /var/cache/apk/* 
  
RUN gem install -N nokogiri -- --use-system-libraries && \
  gem install -N rails --version "$RAILS_VERSION" && \
  echo 'gem: --no-document' >> ~/.gemrc && \
  cp ~/.gemrc /etc/gemrc && \
  chmod uog+r /etc/gemrc && \

  # cleanup and settings
  bundle config --global build.nokogiri  "--use-system-libraries" && \
  bundle config --global build.nokogumbo "--use-system-libraries" && \
  rm -rf /usr/lib/lib/ruby/gems/*/cache/* && \
  rm -rf ~/.gem

EXPOSE 3000

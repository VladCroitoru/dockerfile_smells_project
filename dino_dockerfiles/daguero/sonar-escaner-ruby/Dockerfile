FROM ciricihq/gitlab-sonar-scanner:2.1.0

MAINTAINER Datys

ENV BUILD_PACKAGES="curl-dev ruby-dev build-base git cmake bash" \
    DEV_PACKAGES="zlib-dev libxml2-dev libxslt-dev tzdata yaml-dev postgresql-dev libffi-dev libc-dev" \
    RUBY_PACKAGES="ruby ruby-io-console ruby-json yaml nodejs" \
    RAILS_VERSION="4.2.3"

RUN apk --update --upgrade add $BUILD_PACKAGES $RUBY_PACKAGES $DEV_PACKAGES && \
    gem install -N bundler
    
RUN gem install -N nokogiri -- --use-system-libraries && \
  gem install -N rails --version "$RAILS_VERSION" && \
  echo 'gem: --no-document' >> ~/.gemrc && \
  cp ~/.gemrc /etc/gemrc && \
  chmod uog+r /etc/gemrc && \

  # cleanup and settings
  bundle config --global build.nokogiri "--use-system-libraries" && \ 
  bundle config --global build.nokogumbo "--use-system-libraries" && \ 
  find / -type f -iname \*.apk-new -delete && \ 
  rm -rf /var/cache/apk/* && \ 
  rm -rf /usr/lib/lib/ruby/gems/*/cache/* && \ 
  rm -rf ~/.gem    

RUN gem install rubocop

COPY Dockerfile /

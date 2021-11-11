FROM alpine:3.6

LABEL maintainer="a.maslov@seendex.ru"

ENV BUILD_PACKAGES="curl-dev ruby-dev build-base libffi-dev git" \
    DEV_PACKAGES="zlib-dev libxml2-dev libxslt-dev tzdata yaml-dev postgresql-dev" \
    RUBY_PACKAGES="ruby ruby-io-console ruby-json yaml nodejs ruby-bigdecimal ruby-irb" \
    RAILS_VERSION="5.1.3"

RUN apk --update --upgrade add $BUILD_PACKAGES $RUBY_PACKAGES $DEV_PACKAGES && \
    echo 'gem: --no-document' >> ~/.gemrc && \
    cp ~/.gemrc /etc/gemrc && \
    chmod uog+r /etc/gemrc && \
    gem install -N bundler && \
    gem install -N nokogiri -- --use-system-libraries && \
    gem install -N rails --version "$RAILS_VERSION" && \

    # cleanup and settings
    bundle config --global build.nokogiri  "--use-system-libraries" && \
    bundle config --global build.nokogumbo "--use-system-libraries" && \
    find / -type f -iname \*.apk-new -delete && \
    rm -rf /var/cache/apk/* && \
    rm -rf /usr/lib/lib/ruby/gems/*/cache/* && \
    rm -rf ~/.gem

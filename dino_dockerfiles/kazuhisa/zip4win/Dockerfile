# zip4win Docker files

FROM ruby:2.3.7-alpine
MAINTAINER <ak.hisashi@gmail.com>

RUN apk --update add tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    rm -rf /var/cache/apk/*

ENV BUILD_PACKAGES="curl-dev build-base openssh" \
    DEV_PACKAGES="build-base libxml2-dev libxslt libxslt-dev \
                  sqlite-dev git nodejs"

RUN \
  apk --update --upgrade add $BUILD_PACKAGES $DEV_PACKAGES && \
  rm /var/cache/apk/*

RUN bundle config build.nokogiri --use-system-libraries

# git clone
RUN git clone https://github.com/kazuhisa/zip4win.git

# bundle install
RUN cd /zip4win && bundle install --without development test

# assets precompile
RUN cd /zip4win && bin/rake assets:precompile

# start server
EXPOSE 9292
CMD cd /zip4win && bundle exec puma -e production

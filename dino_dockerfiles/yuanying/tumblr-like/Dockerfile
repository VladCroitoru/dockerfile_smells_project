# docker build -t yuanying/tumblr-like .
# docker run -d -v /volumes/downloads:/usr/src/app/contents yuanying/tumblr-like
FROM ruby:2.5.5-alpine as builder

RUN echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --update add freeimage-dev@community
RUN apk --update add --virtual build-dependencies \
    build-base \
    curl-dev \
    linux-headers
ENV BUNDLER_VERSION 2.0.1
RUN gem install bundler
WORKDIR /tmp
COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock
ENV BUNDLE_JOBS=4
RUN bundle install
RUN apk del build-dependencies

FROM ruby:2.5.5-alpine
MAINTAINER O. Yuanying "yuan-docker@fraction.jp"

ENV BUNDLER_VERSION 2.0.1
RUN gem install bundler
WORKDIR /tmp
COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock
COPY --from=builder /usr/local/bundle /usr/local/bundle

ENV APP_HOME /usr/src/app
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME
COPY . $APP_HOME

VOLUME ["/usr/src/app/contents"]

ENV TUMBLR_CONSUMER_KEY "XXXXX"
ENV TUMBLR_CONSUMER_SECRET "XXXXX"
ENV TUMBLR_CONSUMER_TOKEN "XXXXX"
ENV TUMBLR_CONSUMER_TOKEN_SECRET "XXXXX"

CMD ["bundle", "exec", "ruby", "download.rb"]

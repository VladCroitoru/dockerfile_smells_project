FROM ruby:3.0-alpine

ENV LANG=C.UTF-8
ENV TZ=Asia/Tokyo

# 引数
# nobodyだと動かないかも
# デフォルト引数いらんかな
ARG APP_NAME
ARG WORKDIR
ARG USER=nobody
ARG USER_ID=65534
ARG GROUP=nobody
ARG GROUP_ID=65534

RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
        g++ \
        gcc \
        libc-dev \
        libxml2-dev \
        linux-headers \
        make \
        mariadb-dev \
        nodejs \
        tzdata \
        yarn && \
    apk add --virtual build-packs --no-cache \
        build-base \
        curl-dev && \
    apk del build-packs

WORKDIR $WORKDIR

# railsだけ。rails new で上書き
ADD ./Gemfile $WORKDIR/Gemfile
ADD ./Gemfile.lock $WORKDIR/Gemfile.lock

# ローカル環境のIDと合わせたらいいと思う
RUN addgroup -S -g $GROUP_ID $GROUP && \
    adduser -u $USER_ID -G $USER -D $USER

RUN chown $USER:$GROUP $WORKDIR/*

USER $USER

RUN bundle install

ADD ./ $WORKDIR

# docker-composeで使うことしか考えてないからCMDなし

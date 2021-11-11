FROM ruby:2.6.3
# ベースイメージ 2.6.4じゃなくて2.6.3だよ

ENV RAILS_ENV=production
# 環境変数の設定

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && apt-get update \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update -qq && apt-get install -y build-essential \
  libpq-dev \
  nodejs \
  yarn

RUN mkdir /rails-app

ENV APP_ROOT /rails-app
WORKDIR $APP_ROOT
# 作業をどこでやるかの指定

ADD ./Gemfile $APP_ROOT/Gemfile
ADD ./Gemfile.lock $APP_ROOT/Gemfile.lock

RUN bundle install
ADD . $APP_ROOT
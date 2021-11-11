FROM ruby:2.7.3-buster

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y build-essential tzdata libjpeg62-turbo libpng16-16 libxrender1 libfontconfig1 libxext6

WORKDIR /app
ENV HOME /app

ARG UID='1001'

RUN adduser --uid ${UID}  --disabled-password --gecos "" appuser

RUN chown appuser:appuser /app

COPY --chown=appuser:appuser Gemfile Gemfile.lock .ruby-version ./

RUN gem install bundler

USER appuser

ARG BUNDLE_ARGS='--jobs 4 --deployment --without test development'
RUN bundle install --no-cache ${BUNDLE_ARGS}

COPY --chown=appuser:appuser . .

ARG RAILS_ENV='production'
ENV RAILS_ENV=$RAILS_ENV

ENV APP_PORT 3000
EXPOSE $APP_PORT

CMD bundle exec bundle exec rails s -p ${APP_PORT} --binding=0.0.0.0

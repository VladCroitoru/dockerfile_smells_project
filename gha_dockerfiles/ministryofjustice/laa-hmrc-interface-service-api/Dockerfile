FROM ruby:3.0.2-alpine3.13

MAINTAINER Apply for legal aid team

ENV RAILS_ENV production

RUN set -ex

RUN apk --no-cache add --virtual build-dependencies \
                    build-base \
                    postgresql-dev \
&& apk --no-cache add postgresql-client

RUN mkdir /app
WORKDIR /app

RUN adduser --disabled-password apply -u 1001

COPY Gemfile /app/Gemfile
COPY Gemfile.lock /app/Gemfile.lock

RUN gem install bundler -v 2.2.24 \
&& bundle config build.nokogiri --use-system-libraries \
&& bundle config --global without test:development \
&& bundle install

COPY . /app

RUN apk del build-dependencies

EXPOSE 3000

RUN chown -R apply:apply /app

#RUN chmod +x ./bin/uat_deploy

# expect ping environment variables
ARG BUILD_DATE
ARG BUILD_TAG
ARG APP_BRANCH
# set ping environment variables
ENV BUILD_DATE=${BUILD_DATE}
ENV BUILD_TAG=${BUILD_TAG}
ENV APP_BRANCH=${APP_BRANCH}
# allow public files to be served
ENV RAILS_SERVE_STATIC_FILES true

USER 1001

CMD "./docker_scripts/run"

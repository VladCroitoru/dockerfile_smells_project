FROM ruby:2.7.4-alpine3.12
RUN apk add --update --no-cache tzdata && \
    cp /usr/share/zoneinfo/Europe/London /etc/localtime && \
    echo "Europe/London" > /etc/timezone

RUN apk add --update --no-cache --virtual runtime-dependances \
 yarn \
 openssl-dev

ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD Gemfile $APP_HOME/Gemfile
ADD Gemfile.lock $APP_HOME/Gemfile.lock

RUN apk add --update --no-cache --virtual build-dependances \
 build-base  && \
 bundle install --jobs=4 && \
 apk del build-dependances

ADD package.json $APP_HOME/package.json
ADD yarn.lock $APP_HOME/yarn.lock
RUN yarn install --frozen-lockfile

ADD . $APP_HOME/

RUN bundle exec rake assets:precompile

ARG COMMIT_SHA
ENV COMMIT_SHA=${COMMIT_SHA}

CMD bundle exec rails server -b 0.0.0.0

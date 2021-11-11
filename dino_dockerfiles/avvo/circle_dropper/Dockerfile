FROM avvo/ruby-rails:2.3.3
MAINTAINER Seth Ringling <sringling@avvo.com>

ENV APP_HOME /srv/circle_dropper/current

RUN apk update && \
    apk upgrade && \
    apk add build-base && \
    rm -rf /var/cache/apk/*

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

RUN mkdir -p $APP_HOME/vendor/bundle

ADD Gemfile* $APP_HOME/
ADD vendor/cache $APP_HOME/vendor/cache
RUN bundle install --path vendor/bundle --local --deployment --without development test

ADD . $APP_HOME

ENV RAILS_ENV production
ENV WORKERS 8

ARG BUILD_TIMESTAMP=0
RUN echo $BUILD_TIMESTAMP
ENV BUILD_TIMESTAMP $BUILD_TIMESTAMP

ARG SOURCE_COMMIT=0
RUN echo $SOURCE_COMMIT
ENV COMMIT_HASH $SOURCE_COMMIT

ARG SOURCE_BRANCH=0
RUN echo $SOURCE_BRANCH
ENV GIT_SOURCE_BRANCH $SOURCE_BRANCH

RUN DOCKER_BUILD=true bin/rake assets:precompile

EXPOSE 3000
ENTRYPOINT ["bin/unicorn"]
CMD ["-c", "config/unicorn.rb"]

FROM ruby:2.4-alpine

LABEL "name"="ensemble"
LABEL "version"="0.0.1"

MAINTAINER Hearst Automation Team

# Working directory
ENV APP_HOME /usr/src/rails
ARG BUILD_ENV=prod
ARG RAILS_ENV=production
ARG RACK_ENV=production

RUN mkdir -p $APP_HOME 

WORKDIR $APP_HOME

COPY . $APP_HOME

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories &&\
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories &&\
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories &&\
    apk update && apk add \
    bash \
    supervisor \
    git \
    nodejs \
    openssl-dev \
    libpq \
    postgresql-client \
    libxml2-dev \
    libxslt-dev \
    exim &&\
    runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
            | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
            | sort -u \
            | xargs -r apk info --installed \
            | sort -u \
    )" &&\
    apk add --virtual .ruby-builddeps $runDeps \
    build-base \
    ruby-dev \
    libc-dev \
    sqlite-libs \
    sqlite-dev \
    postgresql-dev \
    linux-headers && \
    gem install bundler &&\
    mkdir -p /var/log/exim &&\
    touch /var/log/exim/mainlog &&\
    chmod 666 /var/log/exim/mainlog &&\
    if [ "${BUILD_ENV}" == 'dev' ]; then bundle install --with development --without test; fi &&\
    if [ "${BUILD_ENV}" == 'prod' ]; then bundle install --without development --without test; fi &&\
    if [ "${BUILD_ENV}" == 'test' ]; then bundle install --with test; fi &&\
    bundle exec rake assets:precompile &&\
    bundle exec rake setup:docker_config["$BUILD_ENV"] &&\
    apk del .ruby-builddeps &&\
    gem cleanup &&\
    rm -rf /var/cache/apk/* &&\
    rm -rf /tmp/*

EXPOSE 3000

CMD ["supervisord", "-c", "/usr/src/rails/supervisord.conf", "-n"]

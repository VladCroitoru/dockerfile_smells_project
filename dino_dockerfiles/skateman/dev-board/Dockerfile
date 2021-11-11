FROM alpine:latest
WORKDIR /usr/src/app

ENV RAILS_ENV production
ENV DEVDEPS g++ ruby-dev make libffi-dev libxml2-dev
ENV RUNDEPS ruby ruby-bundler ruby-irb ruby-json ruby-bigdecimal redis nodejs tzdata

ADD Gemfile /tmp
RUN apk update && \
    apk add $RUNDEPS $DEVDEPS && \
    sed -i 's/daemonize yes/daemonize no/' /etc/redis.conf && \
    echo -e "---\ngem: --no-document" > /etc/gemrc && \
    bundle install --without test development --gemfile=/tmp/Gemfile && \
    mv /tmp/Gemfile.lock /usr/src/app && \
    rm -f /tmp/Gemfile && \
    apk del -r $DEVDEPS

ADD . /usr/src/app
RUN bin/bundle install --without test development && \
    bin/rails assets:precompile && \
    mv config/secrets.tmpl.yml config/secrets.yml && \
    mv Procfile.docker Procfile

CMD foreman start

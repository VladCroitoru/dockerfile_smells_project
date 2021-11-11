FROM alpine:3.11

ENV BUNDLER_VERSION=1.17.3 \
    PORT=3000 \
    PS1="\n\n>> ruby \W \$ " \
    TERM=linux \
    TZ=UTC

RUN apk --no-cache add \
    bash \
    build-base \
    curl \
    curl-dev \
    dcron \
    git \
    libffi-dev \
    nodejs \
    ruby \
    ruby-bigdecimal \
    ruby-dev \
    ruby-full \
    ruby-io-console \
    ruby-irb \
    ruby-json \
    tzdata \
    zlib-dev \
    && \
    echo 'gem: --no-document' > /etc/gemrc && gem install bundler -v ${BUNDLER_VERSION} && \
    bundle config --global silence_root_warning 1

RUN mkdir -p /usr/app/
WORKDIR /usr/app

COPY Gemfile* /usr/app/
RUN bundle install --without development test

COPY . /usr/app/
RUN echo "export BUILD_DATE=`date '+%Y-%m-%d'`" > /set_env

ENTRYPOINT [ "./docker-entrypoint.sh" ]
CMD crond && bundle exec whenever --update-crontab && bundle exec rails s -b 0.0.0.0 -p $PORT

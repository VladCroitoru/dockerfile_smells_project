FROM ruby:2.3.3-alpine
MAINTAINER Per Christian B. Viken <perchr@northblue.org>

RUN addgroup -S errbit \
    && adduser -S -D -s /bin/false -G errbit -g errbit errbit

# throw errors if Gemfile has been modified since Gemfile.lock
RUN echo "gem: --no-document" >> /etc/gemrc \
  && bundle config --global frozen 1 \
  && bundle config --global clean true \
  && bundle config --global disable_shared_gems false

RUN gem update --system \
  && gem install bundler \
  && apk add --no-cache --virtual \
    build-dependencies \
    build-base \
  && apk update && apk add --no-cache \
    ca-certificates \
    openssl \
    curl \
    less \
    libxml2-dev \
    libxslt-dev \
    nodejs \
    tzdata \
    ssmtp

RUN  mkdir -p /app \
       && chown -R errbit:errbit /app \
       && chmod 700 /app/ \
       && wget -O - https://github.com/errbit/errbit/archive/60fd497.tar.gz | tar -xz -C /app \
       && cd /app \
       && find errbit-60fd497e3df576f9af925f56b09a398425babe0b -name ".*" -mindepth 1 -maxdepth 1 -exec mv {} . \; \
       && mv errbit-60fd497e3df576f9af925f56b09a398425babe0b/* . \
       && rmdir errbit-60fd497e3df576f9af925f56b09a398425babe0b

ADD etc/ssmtp.conf "/etc/ssmtp/ssmtp.conf"
ADD etc/crossdomain.xml "/app/public/crossdomain.xml"

WORKDIR /app

RUN bundle config build.nokogiri --use-system-libraries \
    && bundle install \
        -j "$(getconf _NPROCESSORS_ONLN)" \
        --retry 5 \
        --without test development no_docker \
    && apk del build-dependencies

RUN RAILS_ENV=production bundle exec rake assets:precompile \
    && chown -R errbit:errbit /app

USER errbit
EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:$PORT/users/sign_in || exit 1

CMD ["bundle", "exec", "puma", "-C", "config/puma.default.rb"]

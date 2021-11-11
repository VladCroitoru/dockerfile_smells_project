FROM ruby:2.7.3-alpine

# Required apps for common rails application
ENV PACKAGES="\
    git \
    curl \
    postgresql-client \
    imagemagick \
    tzdata \
    yarn \
"

RUN apk add --no-cache $PACKAGES && rm -rf /usr/share/man /tmp/* /var/cache/apk/*

RUN mkdir -p /app
WORKDIR /app

# Install application gems

COPY Gemfile Gemfile.lock /app/

# Build dependencies for gems (will be removed after installation)
ENV BUILD_PACKAGES="\
    libxml2-dev \
    libxslt-dev \
    postgresql-dev \
"

# Build argument for skip "test development" gems in production
ARG BUILD_WITHOUT

# Install gem with installation and removal of gem dependencies and nokogiri build arguments
RUN set -x \
    && apk upgrade --no-cache \
    && apk add --no-cache --virtual build-dependencies \
        build-base \
    && apk add --no-cache \
        $BUILD_PACKAGES \
    && gem install bundler \
    && bundle config build.nokogiri --use-system-libraries \
        --with-xml2-config=/usr/bin/xml2-config \
        --with-xslt-config=/usr/bin/xslt-config \
    && bundle config force_ruby_platform true \
    && bundle install --without test development \
    && apk del build-dependencies \
    && rm -rf /usr/share/man /tmp/* /var/cache/apk/*

# Start your rails app
CMD bundle exec puma -C ./config/puma.rb

COPY bin/ /app/bin/

COPY package.json yarn.lock /app/
RUN bin/yarn install

COPY . /app/

# Precompile assets
RUN RAILS_ENV=production SECRET_KEY_BASE=1 rails assets:precompile
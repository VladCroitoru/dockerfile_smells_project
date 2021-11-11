
# To use or update to a ruby version, change {BASE_RUBY_IMAGE}
ARG BASE_RUBY_IMAGE=ruby:2.7.2-alpine

# BASE_RUBY_IMAGE_WITH_GEMS_AND_NODE_MODULES will defalt to help-for-early-years-gems-node-modules
# building all layers above it if a value is not specified during the build
ARG BASE_RUBY_IMAGE_WITH_GEMS_AND_NODE_MODULES=help-for-early-years-providers-gems-node-modules

# Stage 1: Download gems and node modules
FROM ${BASE_RUBY_IMAGE} AS builder

# Set bundler version
ENV BUNDLER_VERSION=2.2.16

# Dependencies for the build
# git: version manager
# nodejs: JavaScript runtime built on Chrome's V8 JavaScript engine
# yarn: node package manager
# postgresql-dev: postgres driver and libraries
ARG BUILD_DEPS="git gcc libc-dev make nodejs yarn npm shared-mime-info python2 postgresql-dev build-base libxml2-dev libxslt-dev ttf-ubuntu-font-family"

WORKDIR /app

COPY Gemfile Gemfile.lock package.json yarn.lock .ruby-version ./

RUN apk -U upgrade && \
    apk add --update --no-cache --virtual .gem-installdeps $BUILD_DEPS && \
    gem update --system && \
    find / -wholename '*default/bundler-*.gemspec' -delete && \
    rm -rf /usr/local/bundle/bin/bundle && \
    gem install bundler -v ${BUNDLER_VERSION} --no-document && \
    bundler -v && \
    bundle config set no-cache 'true' && \
    bundle config set no-binstubs 'true' && \
    bundle --retry=5 --jobs=4 --without=development test && \
    yarn install --check-files --production && \
    apk del .gem-installdeps && \
    rm -rf /usr/local/bundle/cache && \
    find /usr/local/bundle/gems -name "*.c" -delete && \
    find /usr/local/bundle/gems -name "*.h" -delete && \
    find /usr/local/bundle/gems -name "*.o" -delete

# Stage 2: reduce size of gems-node-modules and only keep required files
# Add the timezone as it's not configured by default in Alpine
FROM ${BASE_RUBY_IMAGE} as help-for-early-years-providers-gems-node-modules

RUN apk -U upgrade && \
    apk add --update --no-cache nodejs yarn tzdata libpq libxml2 libxslt graphviz shared-mime-info && \
    echo "Europe/London" > /etc/timezone && \
    cp /usr/share/zoneinfo/Europe/London /etc/localtime

COPY --from=builder /app /app
COPY --from=builder /usr/local/bundle /usr/local/bundle

# Stage 3: assets-precompile, precompile assets and remove compile dependencies
FROM ${BASE_RUBY_IMAGE_WITH_GEMS_AND_NODE_MODULES} as assets-precompile

ARG RAILS_ENV=production
ENV GOVUK_APP_DOMAIN=www.gov.uk \
    GOVUK_WEBSITE_ROOT=https://www.gov.uk \
    RAILS_ENV=${RAILS_ENV} \
    AUTHORIZED_HOSTS=127.0.0.1 \
    SECRET_KEY_BASE=TestKey \
    IGNORE_SECRETS_FOR_BUILD=1
 
#    RACK_ENV=${RAILS_ENV} \
#    LANG=C.UTF-8 \
#    BUNDLE_JOBS=4 \
#    BUNDLE_RETRY=3 \
#    BUNDLE_PATH=/usr/local/bundle \
#    RAILS_SERVE_STATIC_FILES=true \
#    RAILS_LOG_TO_STDOUT=true \

WORKDIR /app 
COPY . .

RUN bundle exec rake assets:precompile && \
    apk del nodejs yarn && \
    rm -rf yarn.lock && \
    rm -rf tmp/* log/* node_modules /usr/local/share/.cache /tmp/*

# Stage 4: production, copy application code and compiled assets to base ruby image
# Depends on assets-precompile stage which can be cached from a pre-build image
# by specifiying a fully qualified image name or will default to packages-prod
# thereby rebuilding all 3 stages above.
# If an existing base image name is specified Stage 1 & 2 will not be build and
# gems and dev packages will be used from the supplied image.

FROM ${BASE_RUBY_IMAGE} as production
ARG SHA
ENV AUTHORIZED_HOSTS=127.0.0.1 \
    SHA=${SHA}

RUN apk -U upgrade && \
    apk add --update --no-cache tzdata libpq libxml2 libxslt graphviz shared-mime-info && \
    echo "Europe/London" > /etc/timezone && \
    cp /usr/share/zoneinfo/Europe/London /etc/localtime

COPY --from=assets-precompile /app /app 
COPY --from=assets-precompile /usr/local/bundle/ usr/local/bundle/

# The application runs from /app
WORKDIR /app

# Use the following for development testing
# CMD bundle exec rails db:migrate && bundle exec rails server -b 0.0.0.0

# Otherwise use the following
CMD bundle exec rails db:migrate:ignore_concurrent_migration_exceptions && bundle exec rails server -b 0.0.0.0

# We migrate and ignore concurrent_migration_exceptions because we deploy to
# multiple instances at the same time.
#
# Under these conditions each instance will try to run migrations. Rails uses a
# database lock to prevent them stepping on each another. If they happen to,
# a ConcurrentMigrationError exception is thrown, the command exits 1, and
# the server will not start thanks to the shell &&.
#
# We swallow the exception and run the server anyway, because we prefer running
# new code on an old schema (which will be updated a moment later) to running
# old code on the new schema (which will require another deploy or other manual
# intervention to correct).
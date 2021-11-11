FROM ruby:2.7-alpine

# Build information
ARG GIT_OWNER
LABEL git_owner=$GIT_OWNER
ENV GIT_OWNER=$GIT_OWNER

ARG GIT_REPO
LABEL git_repo=$GIT_REPO
ENV GIT_REPO=$GIT_REPO

ARG GIT_BRANCH
LABEL git_branch=$GIT_BRANCH
ENV GIT_BRANCH=$GIT_BRANCH

ARG GIT_COMMIT
LABEL git_commit=$GIT_COMMIT
ENV GIT_COMMIT=$GIT_COMMIT

ARG BUILD_TIME
LABEL build_time=$BUILD_TIME
ENV BUILD_TIME=$BUILD_TIME

ARG CCS_VERSION
LABEL ccs_version=$CCS_VERSION
ENV CCS_VERSION=$CCS_VERSION

ARG APP_RUN_SIDEKIQ
LABEL app_run_sidekiq=$APP_RUN_SIDEKIQ
ENV APP_RUN_SIDEKIQ=$APP_RUN_SIDEKIQ

ARG APP_RUN_NUTS_IMPORT
LABEL app_run_nuts_import=$APP_RUN_NUTS_IMPORT
ENV APP_RUN_NUTS_IMPORT=$APP_RUN_NUTS_IMPORT

ARG APP_RUN_NUTS_IMPORT_IN_BG
LABEL app_run_nuts_import_in_bg=$APP_RUN_NUTS_IMPORT_IN_BG
ENV APP_RUN_NUTS_IMPORT_IN_BG=$APP_RUN_NUTS_IMPORT_IN_BG

ARG APP_UPDATE_NUTS_NOW
LABEL app_update_nuts_now=$APP_UPDATE_NUTS_NOW
ENV APP_UPDATE_NUTS_NOW=$APP_UPDATE_NUTS_NOW

ARG APP_RUN_PC_TABLE_MIGRATION
LABEL app_run_pc_table_migration=$APP_RUN_PC_TABLE_MIGRATION
ENV APP_RUN_PC_TABLE_MIGRATION=$APP_RUN_PC_TABLE_MIGRATION

ARG APP_RUN_POSTCODES_IMPORT
LABEL app_run_postcodes_import=$APP_RUN_POSTCODES_IMPORT
ENV APP_RUN_POSTCODES_IMPORT=$APP_RUN_POSTCODES_IMPORT

ARG APP_RUN_PROCUREMENTS_CLEANUP
LABEL app_run_procurements_cleanup=$APP_RUN_PROCUREMENTS_CLEANUP
ENV APP_RUN_PROCUREMENTS_CLEANUP=$APP_RUN_PROCUREMENTS_CLEANUP

ARG APP_RUN_POSTCODES_CLEANUP
LABEL app_run_postcodes_cleanup=$APP_RUN_POSTCODES_CLEANUP
ENV APP_RUN_POSTCODES_CLEANUP=$APP_RUN_POSTCODES_CLEANUP

ARG APP_RUN_RAKE_TASKS
LABEL app_run_rake_tasks=$APP_RUN_RAKE_TASKS
ENV APP_RUN_RAKE_TASKS=$APP_RUN_RAKE_TASKS

ARG CLAMAV_SERVER_IP
LABEL clam_av_server_ip=$CLAMAV_SERVER_IP
ENV CLAMAV_SERVER_IP=$CLAMAV_SERVER_IP

ARG ASSETS_BUCKET
LABEL assets_bucket=$ASSETS_BUCKET
ENV ASSETS_BUCKET=$ASSETS_BUCKET

ARG APP_RUN_PRECOMPILE_ASSETS
LABEL app_run_precompile_assets=$APP_RUN_PRECOMPILE_ASSETS
ENV APP_RUN_PRECOMPILE_ASSETS=$APP_RUN_PRECOMPILE_ASSETS



##_PARAMETER_STORE_MARKER_##

ENV BUILD_PACKAGES curl-dev ruby-dev postgresql-dev build-base tzdata clamav clamav-daemon

# Update and install base packages
RUN apk update \
    && apk upgrade \
    && apk add bash $BUILD_PACKAGES npm git

RUN npm config set unsafe-perm true

# Install yarn to manage Node.js dependencies
RUN npm install yarn -g

# Throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1 \
    && bundle config set deployment 'true' \
    && bundle config set without 'development test'

# Create app directory
WORKDIR /usr/src/app

COPY Gemfile Gemfile.lock ./

# Install Gem dependencies
RUN bundle install

# Install Node.js dependencies
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile --production --no-cache

COPY . .

# Run app in production environment
ENV RAILS_ENV=production

# Configure Rails to serve the assets
ENV RAILS_SERVE_STATIC_FILES=true

# Send logs to STDOUT so that they can be sent to CloudWatch
ENV RAILS_LOG_TO_STDOUT=true

# Compile assets
RUN GOOGLE_GEOCODING_API_KEY=dummy SECRET_KEY_BASE=dummy APP_RUN_PRECOMPILE_ASSETS="FALSE" bundle exec rails assets:precompile

RUN apk add nginx
RUN mkdir -p /run/nginx
COPY default.conf /etc/nginx/http.d/default.conf

# Run the web app on port 8080
ENV PORT=8080
EXPOSE 8080

# Ensure our entry point script is executable
RUN chmod +x ./bin/docker-entrypoint.sh

ENTRYPOINT ./bin/docker-entrypoint.sh

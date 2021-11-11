# Build the assets
FROM node:lts as node

COPY ./ /app

RUN cd /app \
    && yarn \
    && yarn build

RUN cd /app \
    && rm -rf ./node_modules \
    && rm -rf ./assets \
    && rm -rf ./src/DataFixtures/data

# Install PHP dependencies
FROM composer:latest as composer

ENV APP_ENV=cli

COPY --from=node /app /app

RUN cd /app \
    && composer install --no-dev --ignore-platform-reqs --optimize-autoloader --no-interaction \
    && composer dump-autoload --no-dev --classmap-authoritative --no-interaction \
    && rm -rf ./var

# Build the app image
FROM ghcr.io/mep-agency/symfony-app-runtime:8.0-apache

# Copy source code
COPY --from=composer /app/ /var/www/html/

ARG BUILD_VERSION
ARG COMMIT_HASH

ENV APP_BUILD_VERSION=$BUILD_VERSION
ENV APP_BUILD_COMMIT_HASH=$COMMIT_HASH

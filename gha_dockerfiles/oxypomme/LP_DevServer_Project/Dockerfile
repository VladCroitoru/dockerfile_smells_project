FROM node:lts-alpine AS client-builder

WORKDIR /build

# Add project files
COPY . ./
# Upgrade
RUN apk update \
  && apk upgrade -U -a \
  # Build client
  && if [ -d dist ]; then rm -rf dist; fi \
  && if [ -f .env.prod ]; then mv -f .env.prod .env; fi \
  && npm i \
  && export NODE_ENV=production \
  && npm run build

# ====

FROM php:7.4.3-alpine AS builder

WORKDIR /build

# Add project files
COPY --from=client-builder /build/ ./
# Install composer
COPY --from=composer /usr/bin/composer /usr/bin/composer
# Upgrade
RUN apk update \
  && apk upgrade -U -a \
  && apk add git unzip --no-cache \
  # Install dependencies
  && composer install --no-dev --optimize-autoloader \
  # Make it fetchable
  && mkdir /app \
  && mv dist/ php/ public/ vendor/ .env ./*.php ./composer.json /app/

# ====

FROM php:7.4.24-fpm-alpine

WORKDIR /app

# Add project files
COPY --from=builder /app ./

# Upgrade + install driver
RUN apk update \
  && apk upgrade -U -a \
  && docker-php-ext-install pdo pdo_mysql \
  # Setup start command
  && echo "vendor/bin/doctrine orm:generate-proxies" > start.sh \
  && echo "php-fpm" >> start.sh \
  && chmod +x start.sh

# Run server
CMD ./start.sh

FROM php:8-fpm-buster

WORKDIR /app

ARG APP_ENV=prod
ARG DATABASE_URL=postgresql://database_user:database_password@0.0.0.0:5432/database_name?serverVersion=12&charset=utf8
ARG JWT_SECRET_KEY=jwt_secret_key
ARG JWT_PUBLIC_KEY=jwt_public_key
ARG JWT_PASSPHRASE=jwt_passphrase
ARG PRIMARY_ADMIN_TOKEN=primary-admin-token
ARG SECONDARY_ADMIN_TOKEN=secondary-admin-token
ARG IS_READY=0

ENV APP_ENV=$APP_ENV
ENV DATABASE_URL=$DATABASE_URL
ENV JWT_SECRET_KEY=$JWT_SECRET_KEY
ENV JWT_PUBLIC_KEY=$JWT_PUBLIC_KEY
ENV JWT_PASSPHRASE=$JWT_PASSPHRASE
ENV PRIMARY_ADMIN_TOKEN=$PRIMARY_ADMIN_TOKEN
ENV SECONDARY_ADMIN_TOKEN=$SECONDARY_ADMIN_TOKEN
ENV IS_READY=$READY

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

RUN apt-get -qq update && apt-get -qq -y install  \
  git \
  libpq-dev \
  libzip-dev \
  supervisor \
  zip \
  && docker-php-ext-install \
  pdo_pgsql \
  zip \
  && apt-get autoremove -y \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p var/log/supervisor

COPY build/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY build/supervisor/conf.d/app.conf /etc/supervisor/conf.d/supervisord.conf

COPY composer.json composer.lock /app/
COPY bin/console /app/bin/console
COPY public/index.php public/
COPY src /app/src
COPY config/bundles.php config/services.yaml /app/config/
COPY config/packages/*.yaml /app/config/packages/
COPY config/packages/prod /app/config/packages/prod
COPY config/routes.yaml /app/config/
COPY migrations /app/migrations

RUN chown -R www-data:www-data /app/var/log \
  && composer check-platform-reqs --ansi \
  && echo "APP_SECRET=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)" > .env \
  && composer install --no-dev --no-scripts \
  && rm composer.lock \
  && php bin/console cache:clear

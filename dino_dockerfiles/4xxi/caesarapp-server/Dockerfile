#
# ---- Base Image ----
FROM 4xxi/php-redis:php-7.2.2-fpm-alpine3.7 AS base
# Preparing
RUN mkdir -p /var/www/html && chown -R www-data /var
# Set working directory
WORKDIR /var/www/html
# Run in production mode
ENV APP_ENV=prod
# Copy project file
COPY composer.json .
COPY composer.lock .

#
# ---- Dependencies ----
FROM base AS dependencies
# install vendors
RUN composer global require hirak/prestissimo  --prefer-dist --no-progress --no-suggest --optimize-autoloader  --no-interaction
RUN mkdir -p var/cache var/logs var/sessions
RUN composer install --prefer-dist --no-progress --no-suggest --no-interaction --optimize-autoloader
RUN composer update --lock
# copy production vendor aside
#RUN mv vendor prod_vendor
# install dev vendors
#
# ---- Test & Build ----
# run linters, setup and tests
# FROM dependencies AS sources
# COPY . .
#
# ---- Release ----
FROM base AS release
# copy production vendors
COPY --from=dependencies /var/www/html/vendor ./vendor
COPY . .
# expose port and define CMD
EXPOSE 9000
CMD php-fpm

FROM php:5.5-fpm
# Install modules
RUN apt-get update && apt-get install -y libpq-dev libpq5 \
    && docker-php-ext-install pgsql

CMD ["php-fpm"]
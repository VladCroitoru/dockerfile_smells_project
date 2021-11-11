# All rights reserved © 2018 Zero
FROM php:7.2.2
MAINTAINER Mohos Tamas <tomi@mohos.name>

ENV DEBIAN_FRONTEND="noninteractive"

# Update and install required packages
RUN apt-get update \
    && apt-get -y dist-upgrade \
    && apt-get install -y git curl cron zlib1g-dev libicu-dev g++ rsyslog nano locales locales-all \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-configure intl \
    && docker-php-ext-install zip intl gettext mysqli pdo_mysql exif

# Config
RUN rm -f /etc/localtime \
    && ln -s /usr/share/zoneinfo/Europe/Budapest /etc/localtime \
    && echo "Europe/Budapest" > /etc/timezone \
    && echo "log_errors = On" >> /usr/local/etc/php/php.ini \
    && echo "error_log = /dev/stderr" >> /usr/local/etc/php/php.ini \
    && echo "date.timezone = 'Europe/Budapest'" >> /usr/local/etc/php/php.ini \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && composer create-project --prefer-dist cakephp/app /var/www/html \
    && chmod +x /var/www/html/bin/cake \
    && mkdir /var/www/html/src/Shell/Task \
    && chmod -R 777 /var/www/html/

# Copy custom task
COPY ZeroModelTask.php /var/www/html/src/Shell/Task/
    
# Define workspace
WORKDIR /var/www/html

# Define entrypoint
ENTRYPOINT ["/var/www/html/bin/cake"]




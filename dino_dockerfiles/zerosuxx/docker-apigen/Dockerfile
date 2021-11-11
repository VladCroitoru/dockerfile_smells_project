# All rights reserved © 2018 Zero
FROM php:7.1
MAINTAINER Mohos Tamas <tomi@mohos.name>

ENV DEBIAN_FRONTEND="noninteractive"
ENV COMPOSER_ALLOW_SUPERUSER=1

# Update and install required packages
RUN apt-get update \
    && apt-get -y dist-upgrade \
    && apt-get install -y git curl cron zlib1g-dev libicu-dev g++ rsyslog nano \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-install zip

# Config
RUN rm -f /etc/localtime \
    && ln -s /usr/share/zoneinfo/Europe/Budapest /etc/localtime \
    && echo "Europe/Budapest" > /etc/timezone \
    && echo "log_errors = On" >> /usr/local/etc/php/php.ini \
    && echo "error_log = /dev/stderr" >> /usr/local/etc/php/php.ini \
    && echo "date.timezone = 'Europe/Budapest'" >> /usr/local/etc/php/php.ini \
    && echo "memory_limit = 1024M" >> /usr/local/etc/php/php.ini \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && cd /home \ 
    && echo "{" >> composer.json \
    && echo "\"require\": {\"apigen/apigen\": \"dev-master\", \"roave/better-reflection\": \"dev-master#c87d856\"}" >> composer.json \
    && echo "}" >> composer.json \
    && composer update \
    && chmod +x /home/vendor/bin/apigen
    
# Define workspace
WORKDIR /home/

# Define entrypoint
ENTRYPOINT ["/home/vendor/bin/apigen"]




# Our dependencies ore too old for Composer 2
FROM composer:1 AS composer
FROM phusion/baseimage:0.9.17

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    # Need git for composer, sqlite to import sql, cron for background
    # tasks and ssmtp to avoid having cron pull in a full blown MTA
    # like Exim, and apache, php and extensions
    apt-get -q install -y ssmtp \
    sqlite3 \
    git \
    unzip \
    apache2 php5 php5-sqlite \
    php5-intl php5-curl && \
    # And clean up
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./ /harvester

# Composer for building Harvester.
COPY --from=composer /usr/bin/composer /usr/bin/composer

# REST service app requires mod_rewrite.
RUN a2enmod rewrite && \
    # Link in
    rm -rf /var/www/html && \
    ln -s /harvester/web /var/www/html && \
    # Run composer to install app.
    export HOME=/root && \
    cd /harvester && \
    composer install --optimize-autoloader --classmap-authoritative && \
    # Fix up permissions for webapp.
    chmod a+w -R /harvester/app/cache /harvester/app/logs

# Setup defaults for variables.
ENV HARVESTER_SECRET ThisTokenIsNotSoSecretChangeIt
ENV HARVESTER_HOURS_PER_DAY 7.5
ENV HARVESTER_BILLABILITY_GOAL 75
ENV HARVESTER_HARVEST_USER harvest_account_email@email.com
ENV HARVESTER_HARVEST_PASSWORD secretpassword
ENV HARVESTER_HARVEST_ACCOUNT harvestapp_account_name
ENV SYMFONY_ENV prod

# Fix AllowOverride All for /var/www/html
COPY docker/apache2.conf /etc/apache2/apache2.conf

# Override with custom PHP settings
COPY docker/opcache-config.ini /etc/php5/mods-available/
COPY docker/php-config.ini /etc/php5/mods-available/
RUN php5enmod opcache-config php-config

# Add our crontab.
COPY docker/crontab /etc/cron.d/harvester

# Script for setting up harvester.
COPY docker/harvester /etc/my_init.d/

# Make runit start apache.
COPY docker/apache2.service /etc/service/apache2/run

# And error forwarding.
COPY docker/apache-error-forwarder.service /etc/service/apache-error-forwarder/run

WORKDIR /harvester

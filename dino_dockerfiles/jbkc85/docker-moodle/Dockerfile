FROM php:7.0-apache
MAINTAINER Jason Cameron <jbkc85@gmail.com>

ENV MOODLE_VERSION=32 \
    MOODLE_GITHUB=git://git.moodle.org/moodle.git \
    MOODLE_DESTINATION=/var/www/html

# Download Essential Packages
RUN apt-get update \
    && apt-get install -y libpng12-dev libjpeg-dev libpq-dev \
                          graphviz aspell libpspell-dev git-core \
    && apt-get install -y libicu-dev libxml2-dev libcurl4-openssl-dev \
                          libldap2-dev \
    && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-install intl pdo xmlrpc curl pspell ldap zip pgsql gd opcache soap \
    && docker-php-ext-enable opcache \
    && apt-get clean && rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/*

# Copy in and make default content areas
COPY rootfs /
RUN git clone -b MOODLE_${MOODLE_VERSION}_STABLE --depth 1 ${MOODLE_GITHUB} ${MOODLE_DESTINATION}

RUN mkdir -p /moodle/data && \
    chown -R www-data:www-data /moodle && \
    chmod 2775 /moodle && \
    ln -sf /moodle/conf/config.php ${MOODLE_DESTINATION}/config.php

# Enable mod_rewrite
RUN a2enmod rewrite

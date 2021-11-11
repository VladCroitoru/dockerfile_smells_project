FROM php:7.0.11-fpm

MAINTAINER "Zak Henry" <zak.henry@gmail.com>

RUN mkdir -p /data
WORKDIR /data

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libpq-dev \
    libmcrypt-dev \
    libxml2-dev \
    libyaml-dev \
    python-pip \
    python-dev \
    wget \
    nginx \
    libfreetype6 \
    libjpeg62-turbo \
    libmcrypt4 \
    libpng12-0 \
    libfreetype6-dev \
    libjpeg-dev \
    libpng12-dev \
    --no-install-recommends && \
    rm -r /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove

RUN pip install --upgrade supervisor supervisor-stdout

RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr
RUN docker-php-ext-install mcrypt gd pdo_pgsql mbstring pdo_mysql sockets opcache soap

RUN pecl install xdebug-beta && \
    docker-php-ext-enable xdebug

# Install new relic
RUN mkdir -p /opt/newrelic
WORKDIR /opt/newrelic
RUN wget -r -nd --no-parent -Alinux.tar.gz \
	http://download.newrelic.com/php_agent/release/ >/dev/null 2>&1 \
	&& tar -xzf newrelic-php*.tar.gz --strip=1
ENV NR_INSTALL_SILENT true
ENV NR_INSTALL_PHPLIST /usr/local/bin/
RUN bash newrelic-install install
WORKDIR /
RUN pip install newrelic-plugin-agent
RUN mkdir -p /var/log/newrelic
RUN mkdir -p /var/run/newrelic

# disable New Relic by default (allows enable by ENV VAR at runtime)
RUN mv /usr/local/etc/php/conf.d/newrelic.ini /usr/local/etc/php/conf.d/newrelic.ini.dist

# Configure php
ADD config/memory.ini /opt/etc/memory.ini
ADD config/xdebug.ini /opt/etc/xdebug.ini
ADD config/newrelic.ini /opt/etc/newrelic.ini

RUN cat /opt/etc/memory.ini >> /usr/local/etc/php/conf.d/memory.ini

# Configure nginx
ADD config/nginx.conf /etc/nginx/nginx.conf

# Add supervisor config file
ADD config/supervisord.conf /etc/supervisor/supervisord.conf

# Startup scripts
# supervisord startup script
ADD config/supervisord-start.sh /opt/bin/supervisord-start.sh
RUN chmod u=rwx /opt/bin/supervisord-start.sh
# Nginx startup script
ADD config/nginx-start.sh /opt/bin/nginx-start.sh
RUN chmod u=rwx /opt/bin/nginx-start.sh
# PHP startup script
ADD config/php-start.sh /opt/bin/php-start.sh
RUN chmod u=rwx /opt/bin/php-start.sh

ENTRYPOINT ["/opt/bin/supervisord-start.sh"]
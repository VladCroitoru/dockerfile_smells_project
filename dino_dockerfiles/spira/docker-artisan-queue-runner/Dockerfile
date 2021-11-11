FROM php:7.0.13-cli

MAINTAINER "Zak Henry" <zak.henry@gmail.com>

RUN mkdir -p /data
VOLUME ["/data"]
WORKDIR /data

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libpq-dev \
    libmcrypt-dev \
    libxml2-dev \
    python-pip

RUN pip install --upgrade supervisor supervisor-stdout

RUN docker-php-ext-install mcrypt pdo_pgsql mbstring pdo_mysql sockets opcache soap

# Configure php
ADD config/memory.ini /opt/etc/memory.ini
RUN cat /opt/etc/memory.ini >> /usr/local/etc/php/conf.d/memory.ini

# Add supervisor config file
ADD config/supervisord.conf /etc/supervisor/supervisord.conf

# Queue startup script
ADD config/queue-start.sh /opt/bin/queue-start.sh
RUN chmod u=rwx /opt/bin/queue-start.sh

ENTRYPOINT ["/opt/bin/queue-start.sh"]

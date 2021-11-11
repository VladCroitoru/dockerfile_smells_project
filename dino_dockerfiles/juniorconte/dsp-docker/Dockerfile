FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y curl apache2 php5 php5-common php5-cli php5-curl php5-json php5-mcrypt php5-gd php5-mysql mysql-client git php-pear php5-dev libv8-dev g++ cpp && \
    rm -rf /var/lib/apt/lists/*

RUN pecl install mongo

RUN echo "extension=mongo.so" | tee /etc/php5/mods-available/mongo.ini && \
    php5enmod mongo

RUN pecl install v8js-0.1.3

RUN echo "extension=v8js.so" | tee /etc/php5/mods-available/v8js.ini && \
    php5enmod v8js

RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/servername.conf && \
    a2enconf servername

RUN mkdir -p /opt/dreamfactory/platform && \
    chmod 777 /opt/dreamfactory/platform

ENV DSP_CORE_VERSION 1.9.2
RUN git clone --depth 1 -b $DSP_CORE_VERSION https://github.com/dreamfactorysoftware/dsp-core.git /opt/dreamfactory/platform

WORKDIR /opt/dreamfactory/platform

RUN scripts/installer.sh –cv

RUN a2enmod rewrite

RUN chmod 775 /opt/dreamfactory/platform/web/assets/

RUN rm /etc/apache2/sites-enabled/000-default.conf

RUN php5enmod mcrypt

ADD database.config.php /opt/dreamfactory/platform/config/database.config.php

ADD dsp.conf /etc/apache2/sites-available/dsp.conf
RUN a2ensite dsp

VOLUME ["/var/log/apache2", "/opt/dreamfactory/platform"]

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 80

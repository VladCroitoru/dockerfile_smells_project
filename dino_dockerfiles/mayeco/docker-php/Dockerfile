FROM mayeco/docker-base

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        php5-fpm \
        php5-apcu \ 
        php5-curl \
        php5-gd \
        php5-imagick \
        php5-intl \
        php5-mcrypt \
        php5-mysql \
        php5-gearman \
        php5-redis \
        php5-mongo \
        php5-memcached \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN rm /etc/php5/fpm/pool.d/*

ADD php.pool.conf /etc/php5/fpm/pool.d/

ENV PHP_INI_ENV **None**

ADD ./run.sh /run.sh

RUN chmod +x /run.sh

RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf

WORKDIR /var/www

EXPOSE 9000

CMD ["/run.sh"]

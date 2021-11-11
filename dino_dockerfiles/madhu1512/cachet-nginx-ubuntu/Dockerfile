FROM ubuntu:trusty

MAINTAINER Madhukar Thota <madhukar.thota@gmail.com>

ARG APT_FLAGS_COMMON="-qq -y"
ARG APT_FLAGS_PERSISTANT="${APT_FLAGS_COMMON} --no-install-recommends"
ARG APT_FLAGS_DEV="${APT_FLAGS_COMMON} --no-install-recommends"

ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8 DEBIAN_FRONTEND=noninteractive TERM=xterm

RUN DISTRIB_CODENAME=$(/bin/bash -c 'source /etc/lsb-release && echo $DISTRIB_CODENAME') && \
    locale-gen $LC_ALL && \
    echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d && \
    echo "deb http://us.archive.ubuntu.com/ubuntu/ $DISTRIB_CODENAME multiverse" >> /etc/apt/sources.list && \
    apt-get ${APT_FLAGS_COMMON} update && \
    apt-get ${APT_FLAGS_COMMON} install \
            wget 1>/dev/null && \
    wget -q http://nginx.org/keys/nginx_signing.key -O- | apt-key add - && \
    echo "deb http://nginx.org/packages/ubuntu/ $DISTRIB_CODENAME nginx" >> /etc/apt/sources.list.d/nginx.list && \
    apt-get ${APT_FLAGS_COMMON} update && \
    apt-get ${APT_FLAGS_PERSISTANT} install \
            supervisor \
            ca-certificates php5-fpm php5-curl \
            php5-readline php5-mcrypt sudo \
            php5-mysql php5-apcu php5-cli \
            php5-gd php5-mysql php5-pgsql \
            php5-sqlite wget sqlite git \
            libsqlite3-dev postgresql-client mysql-client \
            supervisor cron nginx 1>/dev/null && \
    apt-get ${APT_FLAGS_COMMON} autoremove && \
    apt-get ${APT_FLAGS_COMMON} clean && \
    rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man /tmp/*

ARG cachet_ver
ENV cachet_ver v2.3.10

COPY conf/php-fpm-pool.conf /etc/php5/fpm/pool.d/www.conf
COPY conf/supervisord.conf /etc/supervisor/supervisord.conf
COPY conf/nginx-site.conf /etc/nginx/conf.d/default.conf

RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
RUN mkdir -p /var/www/html && \
    chown -R www-data /var/www

COPY conf/crontab /tmp/artisan-schedule
COPY entrypoint.sh /sbin/entrypoint.sh

RUN crontab /tmp/artisan-schedule && \
        rm /tmp/artisan-schedule

RUN chmod +x /sbin/entrypoint.sh

RUN adduser www-data sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /var/www/html/
USER www-data

# Install composer
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/composer-setup.php');" && \
    php -r "copy('https://composer.github.io/installer.sig', '/tmp/composer-setup.sig');" && \
    php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) !== trim(file_get_contents('/tmp/composer-setup.sig'))) { unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL; exit(1); }" && \
    php /tmp/composer-setup.php --version=1.1.2 && \
    php -r "unlink('composer-setup.php');"


RUN wget https://github.com/cachethq/Cachet/archive/${cachet_ver}.tar.gz && \
    tar xzvf ${cachet_ver}.tar.gz --strip-components=1 && \
    chown -R www-data /var/www/html && \
    rm -r ${cachet_ver}.tar.gz && \
    php composer.phar require predis/predis && \
    php composer.phar install --no-dev -o && \
    rm -rf bootstrap/cache/*


COPY conf/.env.docker /var/www/html/.env

EXPOSE 80/TCP

VOLUME ["/var/www"]

ENTRYPOINT ["/sbin/entrypoint.sh"]
CMD ["start"]

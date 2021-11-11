FROM ubuntu:xenial

ENV REFRESHED_AT "2017-10-16 14:30:00"

RUN apt-get update \
    && apt-get install software-properties-common -y \
    && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php -y \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get purge -y php5*  \
    && DEBIAN_FRONTEND=noninteractive apt-get purge -y php7*  \
    && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y -q \
        curl          \
        wget          \
        php7.2        \
        php7.2-common \
        php7.2-cli    \
        php7.2-fpm    \
        php7.2-dev    \
        php7.2-curl   \
        php7.2-intl   \
        php7.2-mysql  \
		php7.2-redis  \
		php7.2-bcmath \
		php7.2-mbstring \
		php7.2-gd     \
		php7.2-imagick \
		sudo          \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# gosu is used insted of sudo and exec to ensure the container process get pid 1
ENV GOSU_VERSION 1.9
RUN set -x \
    && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ca-certificates wget \
    && rm -rf /var/lib/apt/lists/* \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -O /usr/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && wget -O /usr/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/bin/gosu.asc /usr/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/bin/gosu.asc \
    && chmod +x /usr/bin/gosu \
    && gosu nobody true \
    && apt-get -y clean

# Install apcu_bc-beta
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y -q \
       php-pear \
       make     \
    && rm -rf /var/lib/apt/lists/* \
    && yes '' | pecl install apcu_bc-beta \
    && apt-get -y purge php-pear make \
    && apt-get -y clean


RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer

RUN echo 'extension=apcu.so' >> /etc/php/7.2/cli/php.ini && \
    echo 'extension=apc.so' >> /etc/php/7.2/cli/php.ini && \
    echo 'extension=apcu.so' >> /etc/php/7.2/fpm/php.ini && \
    echo 'extension=apc.so' >> /etc/php/7.2/fpm/php.ini

ADD opcache.ini /etc/php/7.2/mods-available/opcache.ini

# Add empty ini file. Enables config runtime overriding of parameters
RUN touch /etc/php/7.2/mods-available/devops.ini \
    && ln -s /etc/php/7.2/mods-available/devops.ini /etc/php/7.2/fpm/conf.d/99-devops.ini \
    && ln -s /etc/php/7.2/mods-available/devops.ini /etc/php/7.2/cli/conf.d/99-devops.ini

ADD symfony.pool.conf /etc/php/7.2/fpm/pool.d/

RUN sed -i -e "s/^error_log =/;error_log =/" /etc/php/7.2/fpm/php-fpm.conf && \
    sed -i -e "s/;daemonize = yes/daemonize = no/" /etc/php/7.2/fpm/php-fpm.conf && \
    sed -i -e "/^;error_log =/ a \
error_log = /proc/self/fd/2 " /etc/php/7.2/fpm/php-fpm.conf

RUN mkdir -p /run/php/ && \
    touch /run/php/php7.2-fpm.sock

EXPOSE 9000 3000

ADD runit.sh /

ENTRYPOINT ["/runit.sh"]

CMD ["php-fpm7.2", "--nodaemonize", "--fpm-config", "/etc/php/7.2/fpm/php-fpm.conf"]

WORKDIR /var/www

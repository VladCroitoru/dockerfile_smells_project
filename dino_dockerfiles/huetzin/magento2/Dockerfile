
FROM php:7.1-apache

ENV PHP_MEMORY_LIMIT=4G
ENV PHP_DEFAULT_TIMEZONE=America/Mexico_City
ENV SERVER_DOCROOT=/var/www/html
ENV PUBLIC_KEY=0240f44287e3009842c4679d1e244313
ENV PRIVATE_KEY=a82dc5067b1d30f5fa5c51d079caa2ad
ENV MAGENTO_USER=magento
ENV MAGENTO_VERSION=LATEST

RUN buildDeps=" \
        libsasl2-dev \
        build-essential \
    " \
    runtimeDeps=" \
        vim \
        curl \
        git \
        cron \
        sudo \
        openssh-server\
        supervisor \
        libfreetype6-dev \
        libicu-dev \
        libjpeg-dev \
        libmcrypt-dev \
        libpq-dev \
        libxml2-dev \
        libxslt1-dev \
    " \
    && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y $buildDeps $runtimeDeps \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-install bcmath calendar intl mcrypt opcache pdo_mysql soap zip xsl \
    # && docker-php-ext-install pcntl sockets \
    # && pecl install -o -f xdebug \
    # && docker-php-ext-enable xdebug \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -r /var/lib/apt/lists/* \
    && a2enmod rewrite \
    # && echo "opcache.save_comments=1" >> /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini \
    # && echo "opcache.memory_consumption=512" >> /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini \
    # && echo "opcache.enable_cli=1" >> /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini \
    # && echo "opcache.max_accelerated_files=100000" >> /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini \
    # && echo "opcache.validate_timestamps=0" >> /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini \
    # && echo "opcache.consistency_checks=0" >> /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini \
    && mkdir /var/run/sshd \
    && echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config \
    && useradd -m -d /home/$MAGENTO_USER -s /bin/bash $MAGENTO_USER \
    && usermod -aG sudo $MAGENTO_USER \
    && echo "$MAGENTO_USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \
    && touch /etc/sudoers.d/privacy \
    && mkdir /home/$MAGENTO_USER/.ssh \
    && echo "Defaults        lecture = never" >> /etc/sudoers.d/privacy \
    && sed -i 's/www-data/$MAGENTO_USER/g' /etc/apache2/envvars \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN rm /etc/ssh/sshd_config
COPY etc/sshd_config /etc/ssh/sshd_config

# COPY scripts/cronjobs.sh /home/${MAGENTO_USER}
ADD etc/magento2-cron /etc/cron.d
RUN touch /var/log/cron.log \
    && chmod 775 /var/log/cron.log
RUN chmod 0644 /etc/cron.d/magento2-cron \
    && crontab -u ${MAGENTO_USER} /etc/cron.d/magento2-cron

RUN rm /etc/supervisor/supervisord.conf
COPY etc/supervisord.conf /etc/supervisord.conf

COPY /etc/php.ini /usr/local/etc/php/
COPY /etc/000-default.conf /etc/apache2/sites-available/
COPY /etc/auth.json /home/${MAGENTO_USER}/.composer/
COPY /scripts/instance /usr/local/bin/
COPY entrypoint.sh /usr/local/bin/

RUN passwd $MAGENTO_USER -d

EXPOSE 80 22 5000 44100

WORKDIR ${SERVER_DOCROOT}

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# CMD []



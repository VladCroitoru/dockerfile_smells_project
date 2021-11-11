FROM ubuntu:trusty
MAINTAINER Norbert Mozsar <mozsarn@5net.hu>

# apache
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    software-properties-common \
    python-software-properties \
    supervisor \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN LC_ALL=C.UTF-8 add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) multiverse"

# php
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    git \
    unzip \
    curl \
    apache2 \
    libapache2-mod-rpaf \
    libapache2-mod-fastcgi \
    php7.1-cli \
    php7.1-mbstring \
    php7.1-xml \
    php7.1-soap \
    php7.1-curl \
    php7.1-mcrypt \
    php7.1-gd \
    php7.1-bz2 \
    php7.1-zip \
    php7.1-mysql \
    php7.1-fpm \
    php7.1-sqlite3 \
    php7.1-bcmath \
    php7.1-intl \
    php-xdebug \
    php-redis \
    mysql-client \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    locale-gen hu_HU.UTF-8 && \
    update-locale

RUN a2enmod rewrite && \
    a2enmod rpaf && \
    a2enmod actions && \
    a2enmod fastcgi && \
    a2enmod headers && \
    a2enmod proxy_http && \
    a2disconf other-vhosts-access-log

RUN mkdir /project && \
    phpdismod opcache && \
    curl -o /usr/local/bin/composer https://getcomposer.org/composer.phar && \
    chmod +x /usr/local/bin/composer && \
    composer global require "hirak/prestissimo:^0.3" && \
    composer global require "laravel/installer"

RUN curl -o /tmp/pma.zip https://files.phpmyadmin.net/phpMyAdmin/4.7.0/phpMyAdmin-4.7.0-english.zip && \
    unzip /tmp/pma.zip -d /var/www/ && \
    mv /var/www/phpMyAdmin-4.7.0-english /var/www/phpmyadmin && \
    chmod 755 /var/www/phpmyadmin -R && \
    rm /tmp/pma.zip

COPY files/ /

RUN a2enconf pma.conf && \
    chmod +x /start.sh && \
    mkdir -p /run/php && \
    chmod 777 /run/php && \
    echo "ServerName localhost" >> /etc/apache2/apache2.conf && \
    echo "include=/dev/shm/fpm-user.conf" >> /etc/php/7.1/fpm/pool.d/www.conf && \
    echo "clear_env = no" >> /etc/php/7.1/fpm/pool.d/www.conf

EXPOSE 80

WORKDIR /project

ENV HOME=/tmp

CMD ["/usr/bin/supervisord"]

HEALTHCHECK --interval=5s --timeout=5s --start-period=120s CMD curl -X OPTIONS --fail http://localhost:80/ || exit 1

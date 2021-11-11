FROM ausov/docker-ci-node

RUN export DEBIAN_FRONTEND=noninteractive && \
    export LC_ALL=C.UTF-8 && \
    echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list.d/dotdeb.org.list && \
    echo "deb-src http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list.d/dotdeb.org.list && \
    wget -O- http://www.dotdeb.org/dotdeb.gpg | apt-key add - && \
    apt-get update && \
    apt-get install -y \
        php7.0-sqlite \
        php7.0-curl \
        php7.0-gd \
        php7.0-gmp \
        php7.0-mcrypt \
        php7.0-intl \
        php7.0-dev \
        php7.0-xsl \
        php7.0-xml \
        php7.0-bcmath \
        php-pear && \
  apt-get clean && apt-get autoclean && apt-get --purge -y autoremove && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  curl -sS https://getcomposer.org/installer | php && \
  mv composer.phar /usr/local/bin/composer && \
  chmod a+x /usr/local/bin/composer

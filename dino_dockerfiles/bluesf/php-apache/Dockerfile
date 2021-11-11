FROM php:7.0-apache

# Install PHP extensions and PECL modules.
RUN buildDeps=" \
    libbz2-dev \
    libmemcached-dev \
    default-libmysqlclient-dev \
    libsasl2-dev \
    " \
    runtimeDeps=" \
    vim \
    curl \
    ssmtp \
    git \
    locales \
    libfreetype6-dev \
    libicu-dev \
    libjpeg-dev \
    libmcrypt-dev \
    libmemcachedutil2 \
    libpng-dev \
    libpq-dev \
    libxml2-dev \
    " \
    && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y $buildDeps $runtimeDeps \
    && docker-php-ext-install bcmath bz2 calendar iconv intl mbstring mcrypt mysqli zip \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-install opcache \
    && pecl install redis xdebug mongodb \
    && docker-php-ext-enable redis.so xdebug.so mongodb.so opcache.so \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -r /var/lib/apt/lists/* \
    && a2enmod rewrite actions headers

# Set the locale
RUN sed -i -e 's/# en_US en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen && dpkg-reconfigure locales
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

ENV TZ Asia/Seoul
RUN echo $TZ > /etc/timezone && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime

# Install Composer.
ENV COMPOSER_HOME /root/composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
ENV PATH $COMPOSER_HOME/vendor/bin:$PATH

EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

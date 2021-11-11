FROM php:7.4-fpm
LABEL authors="Nicolas D. <nd@nidum.org> / Simon Baerlocher <s.baerlocher@sbaerlocher.ch>"

ENV TMPDIR=/tmp

# Install all required packages.
RUN apt-get update && \
  apt-get install \
		git \
		libldap2-dev \
		libcurl4-gnutls-dev \
		curl \
		libicu-dev \
		libmcrypt-dev \
		libvpx-dev \
		libjpeg-dev \
		libpng-dev \
		libzip-dev \
		libxpm-dev \
		zlib1g-dev \
		libfreetype6-dev \
		libxml2-dev \
		libexpat1-dev \
		libbz2-dev \
		libgmp3-dev \
		libldap2-dev \
		unixodbc-dev \
		libpq-dev \
		libsqlite3-dev \
		libaspell-dev \
		libsnmp-dev \
		libpcre3-dev \
		libtidy-dev \
		build-essential \
		libkrb5-dev \
		libedit-dev \
		libedit2 \
		gcc \
		make \
		python2.7-dev \
		python-pip \
		re2c \
		wget \
		sqlite3 \
		libmemcached-dev \
		libc-client-dev -yqq \
		libonig-dev \
	&& rm -rf /var/lib/apt/lists/* 
 
# Compile PHP, include these extensions.
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ 
RUN PHP_OPENSSL=yes docker-php-ext-configure imap --with-imap-ssl --with-kerberos --with-imap
RUN docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql
RUN docker-php-ext-install mbstring \
   pdo \
   pdo_pgsql \
   pdo_mysql \
   pdo_sqlite\
   mysqli \
   pgsql \
   json \
   intl \
   gd \
   xml \
   zip \
   bz2 \
   opcache \
   intl \
   bcmath \
   soap \
   ldap \
   imap \
   tokenizer

# Compile and install APCu
RUN pecl install apcu \
    && docker-php-ext-enable apcu
    
# pcntl for Laravel Horizon
RUN docker-php-ext-install pcntl \
    && docker-php-ext-enable pcntl

#install Imagemagick & PHP Imagick ext
RUN apt-get update && apt-get install -y \
  libmagickwand-dev --no-install-recommends
RUN pecl install imagick && docker-php-ext-enable imagick

# Compile and install xDebug
RUN pecl install xdebug \
    && docker-php-ext-enable xdebug 

RUN apt-get update && apt-get install xvfb libgtkextra-dev libnss3 libgconf-2-4 wget gnupg2 -yqq
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install google-chrome-stable -yqq

# Composer
ENV COMPOSER_HOME /usr/local/share/composer
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV PATH "$COMPOSER_HOME:$COMPOSER_HOME/vendor/bin:$PATH"
RUN \
  mkdir -pv $COMPOSER_HOME && chmod -R g+w $COMPOSER_HOME \
  && curl -o /tmp/composer-setup.php https://getcomposer.org/installer \
  && curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \
  && php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) \
    !== trim(file_get_contents('/tmp/composer-setup.sig'))) { unlink('/tmp/composer-setup.php'); \
    echo 'Invalid installer' . PHP_EOL; exit(1); }" \
  && php /tmp/composer-setup.php --filename=composer --install-dir=$COMPOSER_HOME 

# Yarn & Node
RUN apt-get update && apt-get install -yq apt-transport-https
RUN apt-get update && apt-get install -yq  software-properties-common
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get update && apt-get install -yq nodejs
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -yq yarn

# phpunit
RUN wget https://phar.phpunit.de/phpunit.phar
RUN chmod +x phpunit.phar
RUN mv phpunit.phar /usr/local/bin/phpunit

# Clean system up
RUN apt-get -yq upgrade
RUN apt-get -yq autoremove
RUN apt-get -yq clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Deploy improved php.ini
COPY conf/php.ini /usr/local/etc/php/php.ini

# Add user 1000 to www-data
RUN usermod -u 1000 www-data

CMD ["php-fpm"]

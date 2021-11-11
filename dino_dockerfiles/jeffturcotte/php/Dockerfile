FROM php:7.0.7-fpm

RUN apt-get update
RUN apt-get install -y \
	build-essential \
	pkg-config \
	git-core \
	autoconf \
	libjpeg62-turbo-dev \
	libmcrypt-dev \
	libpng12-dev \
	libcurl4-openssl-dev \
	libpq-dev \
	libmemcached-dev \
	libmemcached11 \
	libsqlite3-dev \
	libmagickwand-dev \
	imagemagick \
	subversion \
	python \
	g++ \
	curl \
	vim \
	wget \
	netcat \
	chrpath

RUN docker-php-ext-install iconv
RUN docker-php-ext-install mcrypt
RUN docker-php-ext-install opcache
RUN docker-php-ext-install curl
RUN docker-php-ext-install gd
RUN docker-php-ext-install mysqli
RUN docker-php-ext-install pdo
RUN docker-php-ext-install pdo_pgsql
RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install pdo_sqlite
RUN docker-php-ext-install pgsql
RUN docker-php-ext-install zip

COPY scripts/install-php-memcached.sh /install-php-memcached.sh
RUN bash /install-php-memcached.sh && rm /install-php-memcached.sh

COPY scripts/install-php-imagick.sh /install-php-imagick.sh
RUN bash /install-php-imagick.sh && rm /install-php-imagick.sh

# install composer
WORKDIR /tmp
RUN wget https://getcomposer.org/composer.phar
RUN mv composer.phar /bin/composer
RUN chmod 700 /bin/composer

RUN apt-get clean
RUN apt-get autoremove -y
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/src/*

ADD ./php-fpm.d/www.conf /usr/local/etc/php-fpm.d/www.conf

WORKDIR /var/www/

COPY entrypoint /opt/entrypoint
RUN chmod 755 /opt/entrypoint

ENTRYPOINT ["/opt/entrypoint"]

CMD ["php-fpm"]

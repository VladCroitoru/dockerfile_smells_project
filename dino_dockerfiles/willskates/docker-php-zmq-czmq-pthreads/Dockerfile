FROM		php:5.6.10-cli
MAINTAINER	wlskates12@gmail.com

ENV PHP_VERSION 5.6.10
ENV PHP_INI_DIR /usr/local/etc/php

# --enable-mysqlnd is included below because it's harder to compile after the fact the extensions are (since it's a plugin for several extensions, not an extension in itself)
RUN buildDeps=" \
		$PHP_EXTRA_BUILD_DEPS \
		bzip2 \
		libcurl4-openssl-dev \
		libpcre3-dev \
		libreadline6-dev \
		librecode-dev \
		libsqlite3-dev \
		libssl-dev \
		libxml2-dev \
	" \
	&& set -x \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/* \
	&& curl -SL "http://php.net/get/php-$PHP_VERSION.tar.bz2/from/this/mirror" -o php.tar.bz2 \
	&& curl -SL "http://php.net/get/php-$PHP_VERSION.tar.bz2.asc/from/this/mirror" -o php.tar.bz2.asc \
	&& gpg --verify php.tar.bz2.asc \
	&& mkdir -p /usr/src/php \
	&& tar -xof php.tar.bz2 -C /usr/src/php --strip-components=1 \
	&& rm php.tar.bz2* \
	&& cd /usr/src/php \
	&& ./configure \
		--with-config-file-path="$PHP_INI_DIR" \
		--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \
		$PHP_EXTRA_CONFIGURE_ARGS \
		--disable-cgi \
		--enable-mysqlnd \
		--enable-pcntl \
		--with-curl \
		--with-openssl \
		--with-pcre \
		--with-readline \
		--with-recode \
		--with-zlib \
		--enable-maintainer-zts \
	&& make -j"$(nproc)" \
	&& make install \
	&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip --strip-all '{}' + || true; } \
	&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false $buildDeps \
	&& make clean

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
    && docker-php-ext-install mcrypt mbstring

RUN apt-get install -y git curl wget python-software-properties software-properties-common pkg-config automake libtool checkinstall python-setuptools python-pip build-essential g++

RUN ln -s /usr/bin/libtoolize /usr/bin/libtool

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin
RUN mv /usr/local/bin/composer.phar /usr/local/bin/composer

#Libsodium to help with CURVE security for ZeroMQ
RUN mkdir libsodium
RUN cd libsodium
RUN wget https://github.com/jedisct1/libsodium/releases/download/1.0.2/libsodium-1.0.2.tar.gz
RUN tar -xvzf libsodium-1.0.2.tar.gz
RUN cd /libsodium-1.0.2 && ./autogen.sh
RUN cd /libsodium-1.0.2 && ./configure && make check
RUN cd /libsodium-1.0.2 && checkinstall --install --pkgname libsodium --pkgversion 1.0.0 --nodoc
RUN cd /libsodium-1.0.2 && ldconfig

#Install ZeroMQ
RUN wget http://download.zeromq.org/zeromq-4.1.2.tar.gz -P /tmp
RUN tar -zxvf /tmp/zeromq-4.1.2.tar.gz -C /tmp
RUN cd /tmp/zeromq-4.1.2
RUN cd /tmp/zeromq-4.1.2 && ./autogen.sh
RUN cd /tmp/zeromq-4.1.2 && ./configure
RUN cd /tmp/zeromq-4.1.2 && make
RUN cd /tmp/zeromq-4.1.2 && make install
RUN cd /tmp/zeromq-4.1.2 && ldconfig

#Install mcrypt
RUN apt-get install -y libmcrypt-dev && docker-php-ext-install mcrypt

#Install the pthreads module.
RUN pecl install pthreads-2.0.10
RUN touch /usr/local/etc/php/conf.d/pthreads.ini
RUN echo "extension=pthreads.so" >> /usr/local/etc/php/conf.d/pthreads.ini

#Install the zip extension - for composer
RUN apt-get install -y zlib1g zlib1g-dev
RUN docker-php-ext-install zip

#Install the redis extension
RUN wget -O php-redis.tar.gz https://github.com/phpredis/phpredis/archive/2.2.7.tar.gz
RUN tar -xvzf php-redis.tar.gz
RUN cd phpredis-2.2.7 && phpize
RUN cd phpredis-2.2.7 && ./configure
RUN cd phpredis-2.2.7 && make && make install
RUN touch /usr/local/etc/php/conf.d/redis.ini
RUN echo "extension=redis.so" >> /usr/local/etc/php/conf.d/redis.ini

#Install CZMQ
RUN git clone https://github.com/zeromq/czmq.git /tmp/czmq
RUN cd /tmp/czmq && git checkout v3.0.2
RUN cd /tmp/czmq && ./autogen.sh
RUN cd /tmp/czmq && ./configure && make check
RUN cd /tmp/czmq && make install
RUN cd /tmp/czmq && ldconfig

#Install the php Zeromq extension.
RUN wget https://github.com/mkoppanen/php-zmq/archive/802f326be828b30f413a9c9b2781287a5f5a42ef.tar.gz -P /tmp
RUN tar -zxvf /tmp/802f326be828b30f413a9c9b2781287a5f5a42ef.tar.gz -C /tmp
RUN mv /tmp/php-zmq-802f326be828b30f413a9c9b2781287a5f5a42ef /tmp/php-zmq
RUN cd /tmp/php-zmq && phpize
RUN cd /tmp/php-zmq && ./configure --with-czmq=/tmp/czmq
RUN cd /tmp/php-zmq && make
RUN cd /tmp/php-zmq && make install
RUN touch /usr/local/etc/php/conf.d/zmq.ini
RUN echo "extension=zmq.so" >> /usr/local/etc/php/conf.d/zmq.ini

CMD ["php", "-a"]
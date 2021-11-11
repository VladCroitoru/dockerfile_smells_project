#
# -- SODEF --
#
# BUILD    : DF/[SERVICE][JENKINS][SLAVE/PHP]
# OS/CORE  : debian:8
# SERVICES : jenkins jnkp slave 2.7.4
#
# VERSION 0.9.6
#

FROM jenkinsci/jnlp-slave

MAINTAINER Patrick Paechnatz <patrick.paechnatz@gmail.com>
LABEL com.container.vendor="dunkelfrosch impersonate" \
      com.container.service="df/service/jenkins/php" \
      com.container.priority="1" \
      com.container.project="df-service-jenkins-php-slave" \
      img.version="0.9.6" \
      img.name="local/df/service/jenkins/slave/php/7" \
      img.description="jenkins ci slave service (jnlp) image for dynamic slave build using kubernetes"

# setup some system required environment variables
ENV TIMEZONE           "Europe/Berlin"
ENV TERM                xterm-color
ENV LANG                en_US.UTF-8
ENV NCURSES_NO_UTF8_ACS 1
ENV INITRD              no
ENV LC_ALL              C.UTF-8
ENV DEBIAN_FRONTEND     noninteractive

ENV GPG_KEYS 1A4E8B7277C42E53DBA9C7B9BCAA30EA9C0D5763
ENV PHP_VERSION 7.0.11
ENV PHP_FILENAME php-7.0.11.tar.xz
ENV PHP_SHA256 d4cccea8da1d27c11b89386f8b8e95692ad3356610d571253d00ca67d524c735

ENV PHP_INI_DIR /usr/local/etc/php

# persistent / runtime deps
ENV PHPIZE_DEPS \
		autoconf \
		file \
		g++ \
		gcc \
		libc-dev \
		make \
		pkg-config \
		re2c

# reset default user from jenkins to root for upcoming steps
USER root

# prepare main remote docker helper script path
RUN mkdir -p /opt/docker $PHP_INI_DIR/conf.d

# copy docker script debian cleanup file to docker image
ADD https://raw.githubusercontent.com/dunkelfrosch/docker-bash/master/docker_cleanup_debian.sh /opt/docker/

# x-layer 1: package manager related processor
RUN apt-get update -qq >/dev/null 2>&1 \
    &&  apt-get install -qq -y \
        libfcgi0ldbl mc wget curl ntp sudo \
		$PHPIZE_DEPS \
		ca-certificates librecode0 libedit2 libsqlite3-0 libxml2 xz-utils apt-utils >/dev/null 2>&1

# x-layer 2: prepare php source compilation and add jenkins user to sudo group
RUN set -xe \
    echo "jenkins ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers \
	&& cd /usr/src \
	&& curl -fSL "https://secure.php.net/get/$PHP_FILENAME/from/this/mirror" -o php.tar.xz \
	&& echo "$PHP_SHA256 *php.tar.xz" | sha256sum -c - \
	&& curl -fSL "https://secure.php.net/get/$PHP_FILENAME.asc/from/this/mirror" -o php.tar.xz.asc \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& for key in $GPG_KEYS; do \
		gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
	done \
	&& gpg --batch --verify php.tar.xz.asc php.tar.xz \
	&& rm -r "$GNUPGHOME"

# x-layer 3: copy installation tools for php into target container
COPY docker-php-source /usr/local/bin/

# x-layer 4: install all required sources and tools using apt-*
RUN set -xe \
	&& buildDeps=" \
		$PHP_EXTRA_BUILD_DEPS \
		libcurl4-openssl-dev \
		libedit-dev \
		libsqlite3-dev \
		libssl-dev \
		libxml2-dev \
		zlib1g-dev \
        libreadline6-dev \
        libturbojpeg-dev \
        librecode-dev \
        libmcrypt-dev \
        xz-utils \
	" \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/* \
	\
	&& docker-php-source extract \
	&& cd /usr/src/php \
	&& ./configure \
		--with-config-file-path="$PHP_INI_DIR" \
		--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \
		--with-zlib-dir=/usr \
		--disable-cgi \
		--enable-ftp \
		--enable-mbstring \
		--enable-mysqlnd \
		--with-curl \
		--with-libedit \
		--with-openssl \
		--with-zlib \
        --with-readline \
        --with-recode \
		\
		$PHP_EXTRA_CONFIGURE_ARGS \
	&& make -j"$(nproc)" \
	&& make install \
	&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip --strip-all '{}' + || true; } \
	&& make clean \
	&& docker-php-source delete \
	\
	&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $buildDeps

# x-layer 5: copy additional php source tools to accessable point inside target container
COPY docker-php-ext-* /usr/local/bin/

# x-layer 6: set permission base to build/install helper scripts
RUN chmod +x /usr/local/bin/docker-php-ext-*

# x-layer 8: install extension package dependencies and additional extensions for this slave node
RUN set -e \
    && apt-get update -qq && apt-get install -y --no-install-recommends apt-utils xz-utils libfreetype6-dev libjpeg62-turbo libmcrypt-dev libpng12-dev libssl-dev libcurl4-openssl-dev libsasl2-dev libicu-dev libjpeg-dev

RUN set -e \
    && docker-php-ext-install iconv mcrypt intl mbstring ctype zip exif pdo pdo_mysql \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd

# x-layer 9: install composer globaly
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === 'e115a8dc7871f15d853148a7fbac7da27d6c0030b848d9b3dc09e2a0388afed865e6a3d6b3c0fad45c48e2b5fc1196ae') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
    && php -r "unlink('composer-setup.php');"

# x-layer 10: system core setup related processor
RUN set -e \
    && echo "${TIMEZONE}" >/etc/timezone \
    && dpkg-reconfigure tzdata >/dev/null 2>&1

# x-layer 11: build script cleanUp related processor
RUN set -e \
    && sh /opt/docker/docker_cleanup_debian.sh

# USER jenkins

#
# -- EODEF --
#

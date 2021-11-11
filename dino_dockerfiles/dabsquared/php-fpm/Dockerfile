# See https://github.com/docker-library/php/blob/4677ca134fe48d20c820a19becb99198824d78e3/7.0/fpm/Dockerfile
FROM php:7.2-fpm-alpine

MAINTAINER Daniel Brooks <bass_rock@me.com>


# persistent / runtime deps
RUN apk add --update --no-cache --virtual .persistent-deps \
		ca-certificates \
		curl \
		tar \
		git \
		bash \
		xz \
		bzip2 \
		libbz2 \
		libsodium \
		libpng \
		libjpeg \
		libxml2 \
		libwebp \
		libxslt \
		icu \
		libssh2 \
		libmcrypt \
		freetype \
		curl \
		libcurl \
		pdftk \
		graphviz \
		acl \
		fcgi \
		grep \
		unzip \
# https://github.com/docker-library/php/issues/494
		libressl


# A few reasons for installing distribution-provided OpenJDK:
#
#  1. Oracle.  Licensing prevents us from redistributing the official JDK.
#
#  2. Compiling OpenJDK also requires the JDK to be installed, and it gets
#     really hairy.
#
#     For some sample build times, see Debian's buildd logs:
#       https://buildd.debian.org/status/logs.php?pkg=openjdk-8

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

# add a simple script that can auto-detect the appropriate JAVA_HOME value
# based on whether the JDK or only the JRE is installed
RUN { \
		echo '#!/bin/sh'; \
		echo 'set -e'; \
		echo; \
		echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
	} > /usr/local/bin/docker-java-home \
	&& chmod +x /usr/local/bin/docker-java-home
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin

ENV JAVA_VERSION 8u181
ENV JAVA_ALPINE_VERSION 8.181.13-r0

RUN set -x \
	&& apk add --no-cache \
		openjdk8-jre="$JAVA_ALPINE_VERSION" \
	&& [ "$JAVA_HOME" = "$(docker-java-home)" ]

# If you're reading this and have any feedback on how this image could be
# improved, please open an issue or a pull request so we can discuss it!
#
#   https://github.com/docker-library/openjdk/issues

######Node

ENV NODE_VERSION 10.9.0

RUN addgroup -g 1000 node \
    && adduser -u 1000 -G node -s /bin/sh -D node \
    && apk add --no-cache \
        libstdc++ \
    && apk add --no-cache --virtual .build-deps \
        binutils-gold \
        curl \
        g++ \
        gcc \
        gnupg \
        libgcc \
        linux-headers \
        make \
        python \
  # gpg keys listed at https://github.com/nodejs/node#release-team
  && for key in \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    56730D5401028683275BD23C23EFEFE93C4CFFFE \
    77984A986EBC2AA786BC0F66B01FBB92821C587A \
    8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600 \
  ; do \
    gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
    gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
    gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \
  done \
    && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz" \
    && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
    && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
    && grep " node-v$NODE_VERSION.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
    && tar -xf "node-v$NODE_VERSION.tar.xz" \
    && cd "node-v$NODE_VERSION" \
    && ./configure \
    && make -j$(getconf _NPROCESSORS_ONLN) \
    && make install \
    && apk del .build-deps \
    && cd .. \
    && rm -Rf "node-v$NODE_VERSION" \
    && rm "node-v$NODE_VERSION.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt

ENV YARN_VERSION 1.9.2

RUN apk add --no-cache --virtual .build-deps-yarn curl gnupg tar \
  && for key in \
    6A010C5166006599AA17F08146C2130DFD2497F5 \
  ; do \
    gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
    gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
    gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \
  done \
  && curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \
  && curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \
  && gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \
  && mkdir -p /opt \
  && tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ \
  && ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \
  && ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \
  && rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \
&& apk del .build-deps-yarn

####Our actual php stuff
COPY php.ini /usr/local/etc/php/

RUN apk add --no-cache --virtual .build-php autoconf gcc g++ make bzip2-dev libpng-dev libxml2-dev libxslt-dev libmcrypt-dev icu-dev curl-dev libssh2-dev \
	&& docker-php-ext-install pdo_mysql bcmath bz2 gd xsl intl soap zip calendar pcntl shmop exif opcache \
 	&& pecl install apcu && docker-php-ext-enable --ini-name=20-apcu.ini apcu \
 	&& pecl install apcu_bc && docker-php-ext-enable --ini-name=21-apc.ini apc \
 	&& pecl install ssh2-1.0 && docker-php-ext-enable ssh2 \
 	&& pecl install redis && docker-php-ext-enable redis \
 	&& pecl install mcrypt-1.0.1 && docker-php-ext-enable mcrypt \
 	&& pecl install xdebug && docker-php-ext-enable xdebug \
	&& apk del .build-php


# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer --version

# Set timezone
ENV TZ=Etc/GMT+7
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN date

RUN sed -i 's/9000/3001/' /usr/local/etc/php-fpm.d/zz-docker.conf

# enable xdebug
RUN echo "error_reporting = E_ALL & ~E_NOTICE" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
 && echo "display_startup_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
 && echo "display_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
 && echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
 && echo "xdebug.remote_autostart=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
 && echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
 && echo "xdebug.idekey=\"PHPSTORM\"" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
 && echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
 && echo "xdebug.remote_host=host.docker.internal" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

RUN echo 'alias sf3="php bin/console"' >> ~/.bashrc
RUN echo '{ "allow_root": true }' > ~/.bowerrc

ENV ISDEV=false
ENV ASSECTIC=true
ENV ENVIRONMENT="prod"
ENV DB_DIR=".data/db/"
ENV APP_ENV="prod"
ENV APP_DEBUG=false
ENV APP_FILE="web/app.php"

COPY setup.sh /setup.sh
RUN chmod +x /setup.sh

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

WORKDIR /var/www/symfony
EXPOSE 3001
CMD ["php-fpm"]

HEALTHCHECK  --interval=15s --timeout=3s --retries=30 \
   CMD \
   SCRIPT_NAME=/health \
   SCRIPT_FILENAME=/var/www/symfony/$APP_FILE \
   REQUEST_METHOD=GET \
   cgi-fcgi -bind -connect 127.0.0.1:3001 || exit 1

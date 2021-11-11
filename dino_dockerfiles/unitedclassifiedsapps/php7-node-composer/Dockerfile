FROM alpine:3.6
MAINTAINER Marian Abaffy "marian.abaffy@unitedclassifieds.sk"

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 9.4.0
ENV YARN_VERSION 1.3.2
ENV PHANTOMJS_ARCHIVE="phantomjs.tar.gz"
ENV PHPIZE_DEPS autoconf file g++ gcc libc-dev make pkgconf re2c php7-dev php7-pear \
    yaml-dev pcre-dev zlib-dev libmemcached-dev cyrus-sasl-dev

ADD https://php.codecasts.rocks/php-alpine.rsa.pub /etc/apk/keys/php-alpine.rsa.pub
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories && \
    apk add --update \
    curl \
    bash \
    git \
    unzip \
    wget \
    openssh-client \
    openssh \
    sudo

RUN echo "---> Preparing and Installing PHP" && \
    apk add --update \
    php7 \
    php7-apcu \
    php7-bcmath \
    php7-bz2 \
    php7-curl \
    php7-ctype \
    php7-exif \
    php7-gd \
    php7-imagick \
    php7-imap \
    php7-intl \
    php7-json \
    php7-mbstring \
    php7-mcrypt \
    php7-mysqlnd \
    php7-pdo_mysql \
    php7-mongodb \
    php7-opcache \
    php7-redis \
    php7-soap \
    php7-sqlite3 \
    php7-xdebug \
    php7-xml \
    php7-xmlreader \
    php7-openssl \
    php7-phar \
    php7-zip \
    php7-calendar \
    php7-dba \
    php7-ftp \
    php7-gettext \
    php7-iconv \
    php7-imap \
    php7-ldap \
    php7-odbc \
    php7-pcntl \
    php7-wddx \
    php7-xmlrpc \
    php7-xsl \
    php7-memcached \
    php7-mongodb \
    php7-msgpack \
    php7-xmlwriter \
    php7-tokenizer \
    php7-simplexml \
    php7-zlib && \
    sudo unlink /usr/bin/php && \
    sudo ln -s /usr/bin/php7 /usr/bin/php

COPY php.ini /etc/php7/

RUN echo -e "extension=memcached.so\n" > /etc/php7/conf.d/20_memcached.ini \
    && echo -e ";extension=mongodb.so\n" > /etc/php7/conf.d/mongodb.ini \
    && echo -e "extension=memcache.so\n" > /etc/php7/conf.d/20_memcache.ini \
    && echo -e '\napc.enable_cli = 1\napc.enabled = 1' >> /etc/php7/php.ini

RUN set -xe \
    && apk add --no-cache \
        --virtual .phpize-deps \
        $PHPIZE_DEPS

RUN cd /tmp \
    && wget https://github.com/websupport-sk/pecl-memcache/archive/NON_BLOCKING_IO_php7.zip \
    && unzip NON_BLOCKING_IO_php7.zip \
    && ls /tmp

RUN cd /tmp/pecl-memcache-NON_BLOCKING_IO_php7 \
    && phpize7 \
    && ./configure --with-php-config=/usr/bin/php-config7 \
    && make \
    && make test \
    && make install


RUN echo "---> Installing Composer" && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    echo "---> Cleaning up" && \
    rm -rf /tmp/*

RUN /usr/local/bin/composer global require jakub-onderka/php-parallel-lint && \
    /usr/local/bin/composer global require jakub-onderka/php-var-dump-check && \
    /usr/local/bin/composer global require hirak/prestissimo && \
    /usr/local/bin/composer global require phpunit/phpunit && \
    /usr/local/bin/composer global require phpmd/phpmd && \
    /usr/local/bin/composer global require squizlabs/php_codesniffer && \
    /usr/local/bin/composer global require symfony/phpunit-bridge

RUN /usr/local/bin/composer config --global cache-dir /opt/data/cache/composer/cache-dir
RUN /usr/local/bin/composer config --global cache-vcs-dir /opt/data/cache/composer/cache-vcs-dir
RUN /usr/local/bin/composer config --global cache-repo-dir /opt/data/cache/composer/cache-repo-dir

RUN wget https://github.com/phpDocumentor/phpDocumentor2/releases/download/v2.9.0/phpDocumentor.phar

RUN echo -e "#!/bin/bash\n\nphp /phpDocumentor.phar \$@" >> /usr/local/bin/phpdoc && \
    chmod +x /usr/local/bin/phpdoc

RUN ln -sn /root/.composer/vendor/bin/parallel-lint /usr/local/bin/parallel-lint && \
    ln -sn /root/.composer/vendor/bin/var-dump-check /usr/local/bin/var-dump-check && \
    ln -sn /root/.composer/vendor/bin/phpunit /usr/local/bin/phpunit && \
    ln -sn /root/.composer/vendor/bin/phpmd /usr/local/bin/phpmd && \
    ln -sn /root/.composer/vendor/bin/phpcs /usr/local/bin/phpcs && \
    ln -sn /root/.composer/vendor/bin/phpcs /usr/local/bin/phpunit-bridge

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
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
    56730D5401028683275BD23C23EFEFE93C4CFFFE \
  ; do \
    gpg --keyserver pgp.mit.edu --recv-keys "$key" || \
    gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \
  done \
    && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz" \
    && curl -SLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
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

RUN apk add --no-cache --virtual .build-deps-yarn curl gnupg tar \
  && for key in \
    6A010C5166006599AA17F08146C2130DFD2497F5 \
  ; do \
    gpg --keyserver pgp.mit.edu --recv-keys "$key" || \
    gpg --keyserver keysDockerfileerver.pgp.com --recv-keys "$key" || \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \
  done \
  && curl -fSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \
  && curl -fSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \
  && gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \
  && mkdir -p /opt/yarn \
  && tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \
  && ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \
  && ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \
  && rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \
  && apk del .build-deps-yarn

RUN npm install --global gulp-cli \
    && npm install --global webpack@2 \
    && npm install --global jsdoc \
	&& npm set registry http://npm.i.etech.sk \
	&& npm set progress=false \
	&& npm config set cache /opt/data/cache/npm/cache --global \
	&& npm config set tmp /opt/data/cache/npm/tmp --global

RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/main'>> /etc/apk/repositories \
	&& apk --update add curl

RUN curl -Lk -o $PHANTOMJS_ARCHIVE https://github.com/fgrehm/docker-phantomjs2/releases/download/v2.0.0-20150722/dockerized-phantomjs.tar.gz \
	&& tar -xf $PHANTOMJS_ARCHIVE -C /tmp/ \
	&& cp -R /tmp/etc/fonts /etc/ \
	&& cp -R /tmp/lib/* /lib/ \
	&& cp -R /tmp/lib64 / \
	&& cp -R /tmp/usr/lib/* /usr/lib/ \
	&& cp -R /tmp/usr/lib/x86_64-linux-gnu /usr/ \
	&& cp -R /tmp/usr/share/* /usr/share/ \
	&& cp /tmp/usr/local/bin/phantomjs /usr/bin/ \
	&& rm -fr $PHANTOMJS_ARCHIVE  /tmp/*

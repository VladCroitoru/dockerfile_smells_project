ARG PHP_VERSION=7.1
FROM php:${PHP_VERSION}-cli-jessie

MAINTAINER Anas Ameziane <anasdox@gmail.com>

ENV HOME /tmp

########################
# Install common tools
########################

RUN echo "deb http://deb.debian.org/debian jessie-backports main contrib non-free" >> /etc/apt/sources.list.d/jessie-backports.list && \
    echo "deb http://deb.debian.org/debian jessie-backports-sloppy main contrib non-free" >> /etc/apt/sources.list.d/jessie-backports.list && \
    apt-get update && apt-get -y -t jessie-backports install \
    curl \
    git \
    subversion \
    mercurial \
    openssh-client \
    openssl \
    bash \
    zlib1g-dev \
    build-essential \
    libssl-dev \
    gnupg \
    unzip \
    libpng-dev

########################
# Install composer
########################
ARG COMPOSER_VERSION=1.5.2

ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /tmp
ENV PATH "$PATH:/tmp/vendor/bin"

RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" && echo "date.timezone=${PHP_TIMEZONE:-UTC}" > "$PHP_INI_DIR/conf.d/date_timezone.ini"

RUN docker-php-ext-install zip
RUN docker-php-ext-install gd

RUN set -ex \
  && curl -s -f -L -o /tmp/installer.php https://raw.githubusercontent.com/composer/getcomposer.org/da290238de6d63faace0343efbdd5aa9354332c5/web/installer \
  && php -r " \
    \$signature = '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410'; \
    \$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \
    if (!hash_equals(\$signature, \$hash)) { \
        unlink('/tmp/installer.php'); \
        echo 'Integrity check failed, installer is either corrupt or worse.' . PHP_EOL; \
        exit(1); \
    }" \
  && php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer --version=${COMPOSER_VERSION} \
  && composer --ansi --version --no-interaction \
  && rm -rf /tmp/* /tmp/.htaccess

########################
# Install nodejs and yarn
########################
ARG NODE_VERSION=8.9.0

RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \
  && case "${dpkgArch##*-}" in \
    amd64) ARCH='x64';; \
    ppc64el) ARCH='ppc64le';; \
    s390x) ARCH='s390x';; \
    arm64) ARCH='arm64';; \
    armhf) ARCH='armv7l';; \
    *) echo "unsupported architecture"; exit 1 ;; \
  esac \
  && curl -SLO "https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-$ARCH.tar.xz" \
  && tar -xJf "node-v${NODE_VERSION}-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v${NODE_VERSION}-linux-$ARCH.tar.xz" \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs \
  && echo "NODE VERSION: $(node --version)"

ARG YARN_VERSION=1.3.2

RUN set -ex \
  && curl -fSLO --compressed "https://yarnpkg.com/downloads/${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz" \
  && mkdir -p /opt/yarn \
  && tar -xzf yarn-v${YARN_VERSION}.tar.gz -C /opt/yarn --strip-components=1 \
  && ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \
  && ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \
  && rm yarn-v${YARN_VERSION}.tar.gz \
  && echo "YARN VERSION: $(yarn --version)"

ARG PHPUNIT_VERSION=^7.0
ARG PHPCS_VERSION=^3.2

RUN composer global require phpunit/phpunit ${PHPUNIT_VERSION} && composer global require squizlabs/php_codesniffer ${PHPCS_VERSION}

ENTRYPOINT ["/usr/bin/env"]

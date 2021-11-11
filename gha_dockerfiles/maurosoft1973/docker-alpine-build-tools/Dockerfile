FROM maurosoft1973/alpine

ARG BUILD_DATE
ARG ALPINE_RELEASE
ARG ALPINE_RELEASE_REPOSITORY
ARG ALPINE_VERSION
ARG ALPINE_VERSION_DATE
ARG COMPOSER_VERSION
ARG PHPUNIT_VERSION

LABEL \
    maintainer="Mauro Cardillo <mauro.cardillo@gmail.com>" \
    architecture="amd64/x86_64" \
    alpine-version="$ALPINE_VERSION" \
    build="$BUILD_DATE" \
    org.opencontainers.image.title="alpine-build-tools" \
    org.opencontainers.image.description="Build Tools (PHP, Composer, PHPUnit, Symfony Cli, Yarn and Gulp) Docker image running on Alpine Linux" \
    org.opencontainers.image.authors="Mauro Cardillo <mauro.cardillo@gmail.com>" \
    org.opencontainers.image.vendor="Mauro Cardillo" \
    org.opencontainers.image.url="https://hub.docker.com/r/maurosoft1973/alpine-build-tools/" \
    org.opencontainers.image.source="https://gitlab.com/maurosoft1973-docker/alpine-build-tools" \
    org.opencontainers.image.created=$BUILD_DATE

RUN \
    echo "" > /etc/apk/repositories && \
    echo "https://dl-cdn.alpinelinux.org/alpine/$ALPINE_RELEASE_REPOSITORY/main" >> /etc/apk/repositories && \
    echo "https://dl-cdn.alpinelinux.org/alpine/$ALPINE_RELEASE_REPOSITORY/community" >> /etc/apk/repositories && \
    apk update && \
    apk add --update --no-cache \
    bash \
    curl \
    openssh-client \
    ca-certificates \
    sshpass \
    curl \
    rsync \
    lftp \
    git \
    nano \
    nodejs \
    npm \
    php7-apcu \
    php7-cli \
    php7-common \
    php7-ctype \
    php7-curl \
    php7-dev \
    php7-dom \
    php7-fileinfo \
    php7-iconv \
    php7-intl \
    php7-imagick \
    php7-imap \
    php7-gd \
    php7-json \
    php7-mbstring \
    php7-mcrypt \
    php7-mysqlnd \
    php7-mysqli \
    php7-opcache \
    php7-openssl \
    php7-pdo \
    php7-pdo_mysql \
    php7-pear \
    php7-phar \
    php7-posix \
    php7-session \
    php7-simplexml \
    php7-ssh2 \
    php7-tokenizer \
    php7-xml \
    php7-xmlwriter \
    php7-zip \
    php7-zlib && \
    npm install -g yarn && \
    npm install -g gulp-cli && \
    npm install -g gulp-dart-sass && \
    npm install -g gulp-sourcemaps && \
    npm install -g gulp-csso && \
    npm install -g gulp-autoprefixer && \
    wget https://phar.phpunit.de/phpunit-$PHPUNIT_VERSION.phar  -O /usr/local/bin/phpunit && \
    chmod +x /usr/local/bin/phpunit && \
    wget https://get.symfony.com/cli/installer -O /tmp/installer && \
    chmod +x /tmp/installer && \
    ./tmp/installer && \
    mv /root/.symfony/bin/symfony /usr/local/bin/symfony && \
    rm -rf /tmp/* /var/cache/apk/*

# Install Composer
ADD files/composer.sh /tmp/composer.sh
RUN chmod +x /tmp/composer.sh && /tmp/composer.sh

# Script for restore latest modification time
ADD files/restore_last_git_modified_time.sh /usr/local/sbin/git_restore_last_modified_time
RUN chmod +x /usr/local/sbin/git_restore_last_modified_time

# Copy Remote Commandand Symfony
ADD files/ssh_remote_* /usr/local/sbin/
ADD files/symfony /usr/local/sbin/
RUN chmod +x /usr/local/sbin/*

ADD files/run-alpine-build-tools.sh /scripts/run-alpine-build-tools.sh
RUN chmod +x /scripts/run-alpine-build-tools.sh

VOLUME ["/var/www"]

WORKDIR "/var/www"

ENTRYPOINT ["/scripts/run-alpine-build-tools.sh"]

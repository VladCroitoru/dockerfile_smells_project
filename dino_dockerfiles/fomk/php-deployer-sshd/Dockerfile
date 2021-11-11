FROM php:7.1-alpine

ENV DEPLOYER_VERSION=6.0.5

ENV TZ Europe/Riga

ENV PHPIZE_DEPS \
                autoconf \
                dpkg-dev dpkg \
                file \
                g++ \
                gcc \
                libc-dev \
                make \
                pkgconf \
                re2c

RUN set -xe \
    && apk update --no-cache \
    && apk add --no-cache \
        openssh-client \
        openssh \
        bash \
        git \
        ${PHPIZE_DEPS} \
        postgresql-dev \
        zlib-dev \
    && docker-php-ext-install pdo pdo_pgsql opcache zip \
    && docker-php-ext-enable pdo pdo_pgsql opcache zip \
    && apk del \
        postgresql-libs \
        libsasl \
        db \
        ${PHPIZE_DEPS}

RUN set -xe \
    && apk add --update tzdata \
    && cp /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo "${TZ}" > /etc/timezone \
    && echo "date.timezone=${TZ}" > /usr/local/etc/php/conf.d/timezone.ini \
    && apk del tzdata

RUN curl -L https://deployer.org/releases/v${DEPLOYER_VERSION}/deployer.phar > /usr/local/bin/deployer \
        && chmod +x /usr/local/bin/deployer

RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && chmod +x /usr/local/bin/composer

VOLUME ["/project","$HOME/.ssh", "/app"]

WORKDIR /project

COPY entrypoint /entrypoint

RUN  chmod +x /entrypoint

ENTRYPOINT ["/entrypoint"]

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]




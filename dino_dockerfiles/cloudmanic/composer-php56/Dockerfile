FROM alpine:3.5

MAINTAINER Spicer Mathtews <spicer@cloudmanic.com>

# Essential pkgs
RUN apk add --no-cache openssh-client git tar php5-fpm curl bash vim tini

# Essential php magic
RUN apk add --no-cache php5-curl php5-dom php5-gd php5-ctype php5-zip php5-xml php5-iconv php5-mysql php5-sqlite3 php5-mysqli php5-pgsql php5-json php5-phar php5-openssl php5-pdo php5-mcrypt php5-pdo php5-pdo_pgsql php5-pdo_mysql php5-zlib

ENV PATH "/composer/vendor/bin:$PATH"
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /composer
ENV COMPOSER_VERSION 1.3.2

RUN curl -s -f -L -o /tmp/installer.php https://raw.githubusercontent.com/composer/getcomposer.org/5fd32f776359b8714e2647ab4cd8a7bed5f3714d/web/installer \
 && php -r " \
    \$signature = '55d6ead61b29c7bdee5cccfb50076874187bd9f21f65d8991d46ec5cc90518f447387fb9f76ebae1fbbacf329e583e30'; \
    \$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \
    if (!hash_equals(\$signature, \$hash)) { \
        unlink('/tmp/installer.php'); \
        echo 'Integrity check failed, installer is either corrupt or worse.' . PHP_EOL; \
        exit(1); \
    }" \
 && php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer --version=${COMPOSER_VERSION} \
 && rm /tmp/installer.php \
 && composer --ansi --version --no-interaction

COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod 755 /docker-entrypoint.sh

RUN chmod -R 777 /composer

WORKDIR /www

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["composer"]
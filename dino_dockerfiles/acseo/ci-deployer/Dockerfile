FROM php:7-alpine

LABEL maintainer "nicolas.potier@acseo.fr"

RUN         curl -LO https://deployer.org/releases/v6.6.0/deployer.phar \
            && mv deployer.phar /usr/local/bin/dep \
            && chmod +x /usr/local/bin/dep

RUN         apk --no-cache add openssh-client rsync

ENV         COMPOSER_HOME=/var/composer
COPY        composer-install /tmp/composer-install
RUN         chmod +x /tmp/composer-install
RUN         /tmp/composer-install && \
            rm /tmp/composer-install

RUN         composer global require deployer/recipes --dev

ENTRYPOINT  ["/bin/sh", "-c"]

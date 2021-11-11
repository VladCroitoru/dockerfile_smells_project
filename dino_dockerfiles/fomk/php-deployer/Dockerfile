FROM php:7.1-alpine

ENV DEPLOYER_VERSION=6.0.5

RUN apk update --no-cache \
    && apk add --no-cache \
        openssh-client \
        git

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

CMD ["deployer","--version"]


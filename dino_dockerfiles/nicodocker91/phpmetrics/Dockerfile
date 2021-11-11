FROM php:7.2-fpm-alpine

MAINTAINER "Nicolas Giraud" <nicolas.giraud.dev@gmail.com>

RUN PHP_METRICS_VERSION=$(curl -Ls https://raw.githubusercontent.com/phpmetrics/PhpMetrics/master/.semver | grep -Eo ':(major|minor|patch): *[0-9]+' | grep -Eo '[0-9]+' | tr '\n' '.' | sed 's/.$//') \
    && curl -Ls https://github.com/phpmetrics/PhpMetrics/releases/download/v${PHP_METRICS_VERSION}/phpmetrics.phar > /usr/local/bin/phpmetrics \
    && chmod +x /usr/local/bin/phpmetrics \
    # Install git to be able to run PhpMetrics with option "--git"
    && apk add --no-cache git \
    && rm -rf /var/cache/apk/* /var/tmp/* /tmp/* \
    # Not to have the "too many files" error
    && git config --global --add diff.renames 0

VOLUME ["/data"]
WORKDIR /data/www

ENTRYPOINT ["phpmetrics"]
CMD ["--version"]

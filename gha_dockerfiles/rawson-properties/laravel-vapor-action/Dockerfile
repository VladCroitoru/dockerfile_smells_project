FROM laradock/workspace:latest-7.4

ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /composer
ENV PATH "/composer/vendor/bin:~/.local/bin:$PATH"

# https://github.com/nodesource/distributions/issues/1266
RUN set -xe && \
    apt-get update && \
    apt-get install ca-certificates

RUN set -xe && \
    curl --silent --location https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get update && \
    apt-get install -y --force-yes nodejs \
    php7.4-imagick \
    openssh-client \
    unzip
    # apt-get autoremove && \
    # apt-get autoclean && \
    # apt-get clean && \
    # rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN set -xe && \
    composer global require laravel/vapor-cli && \
    composer clear-cache

# Prepare out Entrypoint (used to run Vapor commands)
COPY vapor-entrypoint /usr/local/bin/vapor-entrypoint

ENTRYPOINT ["/usr/local/bin/vapor-entrypoint"]

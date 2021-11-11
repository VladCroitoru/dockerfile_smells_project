FROM garbee/php-cli
MAINTAINER Jonathan Garbee <jonathan@garbee.me>

ENV COMPOSER_HOME /root/composer
ENV COMPOSER_VERSION master

RUN apt-get update && \
    apt-get install -y git subversion unzip curl && \
    echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini && \
    echo "date.timezone=${PHP_TIMEZONE:-UTC}" > $PHP_INI_DIR/conf.d/date_timezone.ini && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    rm -r /var/lib/apt/lists/*

VOLUME ["/srv"]
WORKDIR /srv

CMD ["-"]
ENTRYPOINT ["composer", "--ansi"]


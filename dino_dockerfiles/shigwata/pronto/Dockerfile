FROM ruby:2

ENV PRONTO_ROOT /data
ENV PRONTO_VERSION 0.9.5

WORKDIR $PRONTO_ROOT

RUN apt-get update -y \
    && apt-get install -y apt-transport-https lsb-release ca-certificates \
    && wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg \
    && echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
    cmake \
    zip \
    unzip \
    php7.2-cli \
    php7.2-xml \
    && rm -rf /var/lib/apt/lists/*

RUN gem install pronto -v $PRONTO_VERSION --no-document && \
    gem install pronto-phpcs --no-document && \
    gem install pronto-phpmd --no-document

ENV COMPOSER_HOME /composer
ENV PATH /composer/vendor/bin:$PATH
ENV COMPOSER_ALLOW_SUPERUSER 1

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN composer global require \
    squizlabs/php_codesniffer \
    phpmd/phpmd

CMD [ "pronto", "run" ]

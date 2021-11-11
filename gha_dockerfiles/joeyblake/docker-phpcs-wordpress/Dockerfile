FROM php:7.3-alpine
LABEL maintainer="joeyblake@gmail.com"

# Install Composer globally - https://github.com/composer/composer

ENV COMPOSER_HOME /composer
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV PATH /composer/vendor/bin:$PATH

RUN curl https://getcomposer.org/installer -o /tmp/composer-setup.php \
    && curl https://composer.github.io/installer.sig -o /tmp/composer-setup.sig \
    && php -r "if (hash_file('SHA384', '/tmp/composer-setup.php') !== trim(file_get_contents('/tmp/composer-setup.sig'))) { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php /tmp/composer-setup.php --1 --no-ansi --install-dir=/usr/local/bin --filename=composer \
    && php -r "unlink('/tmp/composer-setup.php');" \
    && php -r "unlink('/tmp/composer-setup.sig');"

# Required by phpcbf

RUN apk add --update --no-cache patch \
    && rm -rf /var/cache/apk/* /var/tmp/* /tmp/*

RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini

RUN composer create-project wp-coding-standards/wpcs --no-dev
RUN composer require squizlabs/php_codesniffer 3.6.0
ENV PATH=$PATH:/wpcs/vendor/bin

ADD https://github.com/Knucklepuck/kp-cs/archive/master.zip /kp-cs.zip
RUN unzip /kp-cs.zip -d /

RUN phpcs --config-set installed_paths /wpcs,/kp-cs-master && \
    phpcs --config-set colors true && \
    phpcs --config-set show_progress 1

VOLUME ["/scripts"]
WORKDIR /scripts

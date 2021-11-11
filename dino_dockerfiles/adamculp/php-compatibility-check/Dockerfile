# Choose the desired PHP version
# Choices available at https://hub.docker.com/_/php/ stick to "-cli" versions recommended
FROM php:7.3-cli

MAINTAINER Adam Culp <adamculp@uws.net>

ENV TARGET_DIR="/usr/local/lib/php-compatibility-check" \
    COMPOSER_ALLOW_SUPERUSER=1 \
    TIMEZONE=America/New_York \
    PHP_MEMORY_LIMIT=512M

RUN mkdir -p $TARGET_DIR

WORKDIR $TARGET_DIR

COPY composer-installer.sh $TARGET_DIR/
COPY composer-wrapper.sh /usr/local/bin/composer

RUN apt-get update && \
    apt-get install -y wget && \
    apt-get install -y zip && \
    apt-get install -y git && \
    apt-get install -y libxml2-dev && \
    docker-php-ext-install xml

# add php-ast extension needed by etsy/phan
RUN cd $TARGET_DIR && \
    git clone https://github.com/nikic/php-ast.git && \
    cd php-ast && \
    phpize && \
    ./configure --enable-ast && \
    make install && \
    docker-php-ext-enable ast

RUN chmod 744 $TARGET_DIR/composer-installer.sh
RUN chmod 744 /usr/local/bin/composer

# Run composer installation of needed tools
RUN $TARGET_DIR/composer-installer.sh && \
   composer selfupdate && \
   composer require --prefer-stable --prefer-source "hirak/prestissimo:^0.3" && \
   composer require --prefer-stable --prefer-dist \
       "squizlabs/php_codesniffer:^3.0" \
       "phpcompatibility/php-compatibility:^9.0" \
       "sstalle/php7cc:dev-master" \
       "etsy/phan:dev-master"

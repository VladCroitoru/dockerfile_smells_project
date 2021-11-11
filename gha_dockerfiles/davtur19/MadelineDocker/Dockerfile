FROM composer:latest AS build

WORKDIR /app/lib/madeline/

RUN apk add --update g++ autoconf automake libtool libzip-dev curl-dev gmp-dev oniguruma-dev opus-dev libevent-dev cmake linux-headers nghttp2-libs libffi-dev libsodium-dev icu-dev
RUN docker-php-ext-install -j$(nproc) curl gmp mbstring ffi sodium intl sockets pdo pdo_mysql

RUN cd /app/lib/madeline &&\
    wget https://pecl.php.net/get/event-3.0.6.tgz &&\
    tar -xf event-3.0.6.tgz &&\
    cd event-3.0.6 &&\
    phpize &&\
    ./configure &&\
    make -j$(nproc) &&\
    make install &&\
    echo "extension=event.so" |tee /usr/local/etc/php/conf.d/event.ini

RUN cd /app/lib/madeline &&\
    git clone --depth=1 https://github.com/microsoft/mimalloc &&\
    cd mimalloc &&\
    mkdir release &&\
    cd release &&\
    cmake .. -DCMAKE_BUILD_TYPE=Release &&\
    make -j$(nproc) &&\
    make install
    
RUN apk del gcc g++ autoconf automake libtool cmake libzip-dev curl-dev oniguruma-dev linux-headers &&\
    rm -rf /var/cache/apk/* \
    /app/lib/madeline/event-3.0.6.tgz \
    /app/lib/madeline/event-3.0.6 \
    /app/lib/madeline/mimalloc

RUN cd /app/lib/madeline/ &&\
    composer require danog/madelineproto:dev-master

WORKDIR /app/src/madeline/

VOLUME /app/src/madeline/

ENTRYPOINT ["bash", "-c", "cd /app/lib/madeline; composer update; cd /app/src/madeline/; LD_PRELOAD=/usr/lib/libmimalloc.so php main.php"]

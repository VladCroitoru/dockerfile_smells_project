FROM php:5.6-cli
RUN apt-get update && apt-get install -y \
        libldap2-dev \
        libjpeg62-turbo-dev \
        libldb-dev \

    && ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \
    && ln -s /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/liblber.so \
    && docker-php-ext-install -j$(nproc) ldap

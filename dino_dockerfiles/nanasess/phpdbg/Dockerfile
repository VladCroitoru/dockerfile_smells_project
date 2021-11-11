FROM php:latest

RUN echo "deb http://cdn.debian.net/debian/ stretch main contrib non-free" > /etc/apt/sources.list.d/mirror.jp.list
RUN echo "deb http://cdn.debian.net/debian/ stretch-updates main contrib" >> /etc/apt/sources.list.d/mirror.jp.list

RUN /bin/rm /etc/apt/sources.list

RUN apt-get update && apt-get remove -y --purge libicu57 libicu-dev && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# apt-get and system utilities
RUN apt-get update && apt-get install -y \
    curl apt-utils apt-transport-https debconf-utils gcc build-essential zlib1g-dev git libpq-dev g++ icu-devtools libxml2-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y libicu-dev=57.1-6+deb9u1 \
    && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \
    && docker-php-ext-install -j$(nproc) pgsql pdo_pgsql zip intl

# install necessary locales
RUN apt-get update && apt-get install -y locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen


RUN curl -sS https://getcomposer.org/installer | \
    php -- --install-dir=/usr/local/bin --filename=composer

# ENTRYPOINT ["docker-php-entrypoint"]
CMD ["phpdbg"]

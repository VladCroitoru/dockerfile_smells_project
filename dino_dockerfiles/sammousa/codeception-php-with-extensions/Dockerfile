FROM alpine:edge

MAINTAINER Sam Mousa <sam@mousa.nl>

RUN apk add --update --no-cache \
    curl \
    git \
    openssh-client \
    php7 \
    php7-ctype \
    php7-curl \
    php7-dom \
    php7-fileinfo \
    php7-gd \
    php7-iconv \
    php7-intl \
    php7-json \
    php7-mbstring \
    php7-mcrypt \
    php7-pcntl \
    php7-pcntl \
    php7-pdo \
    php7-pdo_mysql \
    php7-pdo_sqlite \
    php7-phar \
    php7-posix \
    php7-session \
    php7-soap \
    php7-sockets \
    php7-sockets \
    php7-tokenizer \
    php7-phpdbg \
    php7-xml \
    php7-xmlreader \
    php7-xmlwriter \
    php7-zip \
    php7-zlib \
    poppler-utils \
    tini \
    mysql-client


# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/bin --filename=composer && \
    composer global config bin-dir /bin && \
    composer global config vendor-dir /vendor

# Install php wait-for-it
RUN cd /tmp && \
    git clone  --depth=1 --branch v0.7.1 https://github.com/SAM-IT/wait-for-it-php.git && \
    cd wait-for-it-php && \
    composer install && \
    php -d phar.readonly=0 build.php && \
    cp wait-for-it.phar /bin/wait-for-it && \
    rm -rf /tmp/*

RUN composer global require codeception/codeception
# Test if paths are OK
RUN /sbin/tini -- /bin/codecept
ENTRYPOINT ["/sbin/tini", "--", "/bin/codecept"]
WORKDIR /project
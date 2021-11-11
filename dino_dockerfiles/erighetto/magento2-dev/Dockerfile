FROM php:7.4-apache

ENV APACHE_DOCUMENT_ROOT=/var/www/html  \
    APACHE_PORT=80 \
    APACHE_SECURE_PORT=443 \
    APACHE_SERVER_NAME=default \
    APACHE_HTTP2=1 \
    MSMTP_SERVER=mailhog \
    MSMTP_PORT=1025 \
    PHP_MEMORY_LIMIT=756M \
    PHP_MAX_EXECUTION_TIME=18000 \
    PHP_UPLOAD_MAX_FILESIZE=64M \
    PHP_POST_MAX_SIZE=64M \
    PHP_IDE_CONFIG="serverName=localhost"

RUN apt-get update && apt-get install -y \
    cron \
    default-mysql-client \
    git \
    libfreetype6-dev \
    libicu-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libonig-dev \
    libpng-dev \
    libxslt1-dev \
    libwebp-dev \
    libzip-dev \
    lynx \
    msmtp \
    nano \
    nghttp2 \
    psmisc \
    unzip \
    wget \
    zip

RUN docker-php-ext-configure gd --enable-gd --with-freetype --with-jpeg --with-webp; \
    docker-php-ext-configure intl; \
	docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd; \
	docker-php-ext-configure zip; \
	docker-php-ext-install -j "$(nproc)" \
    bcmath \
    gd \
    intl \
    mbstring \
    pdo_mysql \
    xsl \
    zip \
    opcache \
    soap \
    sockets

RUN pecl install xdebug redis \
    && docker-php-ext-enable xdebug redis \
    && docker-php-source delete

RUN apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*    

COPY docker-php-entrypoint /usr/local/bin/

RUN chmod +x /usr/local/bin/docker-php-entrypoint

RUN usermod -u 1000 www-data; \
    a2enmod rewrite ssl http2;
    
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer; \
    curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig; \
    php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) !== trim(file_get_contents('/tmp/composer-setup.sig'))) { unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL; exit(1); }"; \
    php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin --filename=composer; \
    rm /tmp/composer-setup.php; \
    chmod +x /usr/local/bin/composer;

RUN curl -o n98-magerun2.phar https://files.magerun.net/n98-magerun2-latest.phar; \
    chmod +x ./n98-magerun2.phar; \
    mv n98-magerun2.phar /usr/local/bin/n98-magerun;    

RUN gotpl_url="https://github.com/wodby/gotpl/releases/download/0.1.5/gotpl-alpine-linux-amd64-0.1.5.tar.gz"; \
    wget -qO- "${gotpl_url}" | tar xz -C /usr/local/bin;

COPY templates /etc/gotpl/

COPY .bashrc /root/.bashrc

EXPOSE 80 443 9000

WORKDIR /var/www/html

FROM wordpress:fpm

RUN apt-get update && \
    apt-get -y install \
        unzip \
    && rm -rf /var/lib/apt/lists/*

RUN echo 'php_admin_value[memory_limit] = 160M' >> /usr/local/etc/php-fpm.d/www.conf \
    && echo 'php_admin_value[upload_max_filesize] = 100M' >> /usr/local/etc/php-fpm.d/www.conf \
    && echo 'php_admin_value[post_max_size] = 100M' >> /usr/local/etc/php-fpm.d/www.conf

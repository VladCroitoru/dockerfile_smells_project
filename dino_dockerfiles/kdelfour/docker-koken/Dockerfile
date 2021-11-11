FROM php:7.0-apache

RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >> /etc/apt/sources.list
RUN echo "deb-src http://www.deb-multimedia.org jessie main non-free" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y --force-yes libmcrypt-dev \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng12-dev \
        ffmpeg \
        curl \
        unzip \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd pdo mysqli

RUN echo \
    "upload_max_filesize=500M;\n" \
    "post_max_size=500M;" \
    >> /usr/local/etc/php/conf.d/uploads.ini

VOLUME /var/www/html

RUN curl -fsSL -o /usr/local/src/Koken_Installer.zip \
        "https://s3.amazonaws.com/koken-installer/releases/Koken_Installer.zip" \
    && unzip -d /usr/local/src /usr/local/src/Koken_Installer.zip \
    && rm /usr/local/src/Koken_Installer.zip

COPY docker-entrypoint.sh /usr/local/bin
RUN chmod 775 /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["apache2-foreground"]

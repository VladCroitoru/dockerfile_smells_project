FROM fanningert/docker-caddy
LABEL maintainer fanningert <thomas@fanninger.at>

RUN apk update
RUN apk add php7 php7-fpm
# Nextcloud depends
RUN apk add php7-ctype php7-curl php7-dom php7-fileinfo php7-gettext php7-gd php7-iconv php7-intl php7-json php7-mbstring php7-openssl php7-session php7-simplexml php7-xml php7-xmlreader php7-xmlwriter php7-zip php7-zlib php7-posix libzip php7-pcntl php7-imap
# Extra depends
RUN apk add php7-bcmath php7-exif php7-opcache php7-pear php7-apcu php7-tokenizer php7-doc
# DB depends
RUN apk add php7-pdo php7-pdo_mysql php7-pdo_sqlite php7-mysqlnd php7-sqlite3 php7-pdo_pgsql php7-pgsql

# Clean up apk cache
RUN rm -rf /var/cache/apk/*

ADD root/ /

RUN chmod -v +x /etc/services.d/*/run /etc/cont-init.d/*

RUN mv /etc/php7/php.ini /app/php.ini
RUN mv /etc/php7/php-fpm.d/www.conf /app/php-fpm_www.conf

# Replace PHP-FPM user
RUN /bin/sed -i -- 's/user = nobody/user = app/g' /app/php-fpm_www.conf
RUN /bin/sed -i -- 's/group = nobody/group = users/g' /app/php-fpm_www.conf


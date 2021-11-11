FROM alpine

WORKDIR /root/app

COPY src          src
COPY autoload.php autoload.php
COPY target       target
COPY uppm.json    uppm.json

RUN \
    apk add php8 php8-common wget bash \
    php8-bcmath php8-bz2 php8-calendar php8-cgi \
    php8-common php8-ctype php8-curl php8-dba \
    php8-doc php8-dom php8-embed \
    php8-enchant php8-exif php8-ffi php8-fileinfo \
    php8-fpm php8-ftp php8-gd php8-gettext \
    php8-gmp php8-iconv \
    php8-imap php8-intl \
    php8-ldap php8-litespeed php8-mbstring \
    php8-mysqli php8-mysqlnd php8-odbc \
    php8-opcache php8-openssl php8-pcntl php8-pdo \
    php8-pdo_dblib php8-pdo_mysql php8-pdo_odbc \
    php8-pdo_pgsql php8-pdo_sqlite php8-pear php8-pgsql \
    php8-phar php8-posix php8-pspell php8-session php8-shmop php8-simplexml \
    php8-snmp php8-soap php8-sockets \
    php8-sodium php8-sqlite3 php8-sysvmsg \
    php8-sysvsem php8-sysvshm php8-tidy \
    php8-tokenizer php8-xml php8-xmlreader \
    php8-xmlwriter php8-xsl php8-zip;\
    ln /usr/bin/php8 /usr/bin/php; \
    echo phar.readonly = Off >> /etc/php8/php.ini; \
    php target/uppm.phar lock; \
    php target/uppm.phar install; \
    php src/main/bootstrap.php build; \
    mv target/uppm.phar /usr/local/bin/uppm; \
    chmod +x /usr/local/bin/uppm;
From alpine:latest
MAINTAINER kunalgautam - https://github.com/KunalGautam

# Timezone
ENV TIMEZONE            Asia/Kolkata
ENV PHP_MEMORY_LIMIT    512M
ENV MAX_UPLOAD          256M
ENV PHP_MAX_FILE_UPLOAD 200
ENV PHP_MAX_POST        256M

# install mysql, apache and php and php extensions, tzdata, wget
RUN echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    apk update && \
    apk add \
    bash \
    mysql mysql-client \
    apache2 \
    curl wget \
    tzdata \
    php5-apache2 \
    php5-cli \
    php5-phar \
    php5-zlib \
    php5-zip \
    php5-bz2 \
    php5-ctype \
    php5-mysqli \
    php5-mysql \
    php5-pdo_mysql \
    php5-opcache \
    php5-pdo \
    php5-json \
    php5-curl \
    php5-gd \
    php5-gmp \
    php5-mcrypt \
    php5-openssl \
    php5-dom \
    php5-xml \
    php5-iconv 

#RUN curl -sS https://getcomposer.org/installer | \
#   php -- --install-dir=/usr/bin --filename=composer
    
# configure timezone, mysql, apache
RUN cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    echo "${TIMEZONE}" > /etc/timezone && \
    ln -s /usr/lib/libxml2.so.2 /usr/lib/libxml2.so && \
    sed -i 's#AllowOverride None#AllowOverride All#' /etc/apache2/httpd.conf && \
    sed -i 's#ServerName www.example.com:80#\nServerName localhost:80#' /etc/apache2/httpd.conf && \
    sed -i 's#^DocumentRoot ".*#DocumentRoot "/www"#g' /etc/apache2/httpd.conf && \
    sed -i 's#/var/www/localhost/htdocs#/www#g' /etc/apache2/httpd.conf && \
    sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i" /etc/php5/php.ini && \
    sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i" /etc/php5/php.ini && \
    sed -i "s|;*upload_max_filesize =.*|upload_max_filesize = ${MAX_UPLOAD}|i" /etc/php5/php.ini && \
    sed -i "s|;*max_file_uploads =.*|max_file_uploads = ${PHP_MAX_FILE_UPLOAD}|i" /etc/php5/php.ini && \
    sed -i "s|;*post_max_size =.*|post_max_size = ${PHP_MAX_POST}|i" /etc/php5/php.ini && \
    sed -i "s|;*cgi.fix_pathinfo=.*|cgi.fix_pathinfo= 0|i" /etc/php5/php.ini && \
    mkdir -p /run/apache2 && \
    chown -R apache:apache /run/apache2 && \
    mkdir /www && \
    echo "<?php phpinfo(); ?>" > /www/index.php && \
    chown -R apache:apache /www

# Configure xdebug
RUN echo "zend_extension=xdebug.so" > /etc/php5/conf.d/xdebug.ini && \ 
    echo -e "\n[XDEBUG]"  >> /etc/php5/conf.d/xdebug.ini && \ 
    echo "xdebug.remote_enable=1" >> /etc/php5/conf.d/xdebug.ini && \  
    echo "xdebug.remote_connect_back=1" >> /etc/php5/conf.d/xdebug.ini && \ 
    echo "xdebug.idekey=PHPSTORM" >> /etc/php5/conf.d/xdebug.ini && \ 
    echo "xdebug.remote_log=\"/tmp/xdebug.log\"" >> /etc/php5/conf.d/xdebug.ini


RUN mkdir /docker-entrypoint-initdb.d

# comment out a few problematic configuration values
# don't reverse lookup hostnames, they are usually another container
RUN sed -ri 's/^user\s/#&/' /etc/mysql/my.cnf 
RUN rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld 
RUN chown -R mysql:mysql /var/lib/mysql /var/run/mysqld 
# ensure that /var/run/mysqld (used for socket and lock files) is writable regardless of the UID our mysqld instance ends up having at runtime
RUN chmod 777 /var/run/mysqld
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \
    && echo -e 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]" && c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \
    && mv /tmp/my.cnf /etc/mysql/my.cnf
RUN mysql_install_db --user=mysql --verbose=1 --basedir=/usr --datadir=/var/lib/mysql --rpm > /dev/null 



RUN rm -rf /tmp/src
RUN rm -rf /var/cache/apk/*

WORKDIR /www

EXPOSE 80
EXPOSE 3306

VOLUME ["/www","/var/lib/mysql", "/var/log/apache2/", "/etc"]

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

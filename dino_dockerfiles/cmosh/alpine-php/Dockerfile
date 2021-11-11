FROM alpine:edge
ARG phpmemory_limit=-1
LABEL org.label-schema.name="Alpine-php" \
      org.label-schema.description="Alpine php7 image" \
      org.label-schema.vcs-url="https://github.com/cmosh/alpine-php"

RUN echo http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories  && \
    apk add --no-cache \
    apache2 \
    curl \
    php7 \
    php7-apache2 \
    php7-ctype \     
    php7-curl \     
    php7-dom \    
    php7-gd \     
    php7-iconv \
    php7-intl \    
    php7-json \
    php7-mbstring \
    php7-mcrypt \ 
    php7-mongodb \
    php7-opcache \
    php7-openssl \
    php7-pdo \     
    php7-phar \     
    php7-posix \
    php7-redis \
    php7-session \
    php7-tokenizer \
    php7-xml \
    php7-xmlwriter \             
    php7-xsl \
    php7-zlib && \
    mkdir -p /run/apache2 && \
    mkdir -p /var/log/apache2 && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer && \
    sed -i 's/memory_limit = .*/memory_limit = '${phpmemory_limit}'/' /etc/php7/php.ini

WORKDIR /var/www/localhost
COPY apache.conf /conf/apache.conf
ONBUILD COPY . /var/www/localhost
ONBUILD RUN composer install && \
            chown -R apache:apache /var/www && \
            chown -R apache:apache /run && \
            chown -R apache:apache /var/log/apache2 && \
            chown -R apache:apache /var/www/logs && \
            chmod -R 775 /var/www/logs && \
            find /var/www -type f -exec chmod 664 {} \;   && \  
            find /var/www -type d -exec chmod 775 {} \;   && \
            chmod -R ug+rwx /var/log/apache2 /var/www/logs /var/www/localhost/storage /var/www/localhost/bootstrap/cache 
ONBUILD USER apache
CMD ["httpd","-DFOREGROUND","-f","/conf/apache.conf"]
# Use Alpine Linux
FROM tarzan79/alpine-php-fpm:latest

ENV VERSION 4.7.3

RUN apk update && \
    apk add unzip

RUN mkdir -p /var/www/sites/wordpress && \
    cd /var/www/sites
    
RUN curl -L -O http://wordpress.org/wordpress-${VERSION}.tar.gz
    
RUN tar -xzvf wordpress-${VERSION}.tar.gz -C /var/www/sites && \
    rm wordpress-${VERSION}.tar.gz

#RUN chown -R www-data:www-data /var/www/sites
RUN find /var/www -type d -exec chmod 755 {} + && \
    find /var/www -type f -exec chmod 644 {} +
    
VOLUME ['/var/www/sites/wordpress']
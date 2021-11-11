FROM alpine:3.6
RUN apk -U add ca-certificates nginx git openssl tar \
        php5-fpm php5-json php5-zlib php5-openssl php5-pdo php5-pdo_mysql php5-gd \
        php5-iconv php5-mcrypt php5-curl php5-opcache php5-intl php5-phar php5-xml php5-dom php5-ctype && \
        rm -rf /var/cache/apk/*
ADD https://s3.amazonaws.com/gitlist/gitlist-master.tar.gz /var/www/
ADD config.ini /var/www/gitlist/
RUN cd /var/www; tar -zxvf gitlist-master.tar.gz && \
        chmod -R 777 /var/www/gitlist && \
        cd /var/www/gitlist/; mkdir cache; chmod 777 cache
ADD nginx.conf /etc/
#ADD php7-fpm.conf /etc/php7/
RUN mkdir -p /repos/sentinel && chown -R 1001:0 /repos/sentinel && \
        cd /repos/sentinel; git --bare init . && \
        #echo "security.limit_extensions = " >> /etc/php5/php-fpm.conf && \
        chmod -R 775 /repos && \
        chmod -R 775 /var/log && \
        chmod -R 775 /var/tmp && \
        chmod -R 775 /var/lib/nginx && \
        chown -R 1001:0 /var/log && \
        chown -R 1001:0 /var/tmp && \
        chown -R 1001:0 /var/lib/nginx

WORKDIR /var/www/gitlist/
USER 1001
EXPOSE 8080
CMD php-fpm5 --fpm-config /etc/php5/php-fpm.conf; nginx -c /etc/nginx.conf



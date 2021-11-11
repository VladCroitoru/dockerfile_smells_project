FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive
RUN mkdir -p /run/php

RUN apt -y update && \
    apt -y install php-fpm php-opcache php-curl php-mbstring php-dev php-xml php-gd php-bcmath nginx curl python

ADD conf/ /conf
RUN mv /conf/nginx.conf /etc/nginx/sites-enabled/default && \
    mv /conf/php.ini /etc/php/7.2/fpm/php.ini && \
    mv /conf/www.conf /etc/php/7.2/fpm/pool.d/www.conf && \
    mv /conf/entrypoint /entrypoint && \
    chmod +x /entrypoint && \
    mkdir /var/cache/php && \
    chmod 0777 /var/cache/php && \
    rm -rf /conf

ADD app/ /var/www/html/app
ADD file-manager /var/www/html/file-manager
ADD flag /flag

RUN rm -rf /var/www/html/app/storage/app/public/* /var/www/html/app/storage/logs/*.log /var/www/html/app/tests /var/www/html/app/vendor/ciscn/fm && \
    cp /var/www/html/app/public/check-normal.bak /var/www/html/app/public/check-normal.php && \
    ln -s /var/www/html/file-manager/ /var/www/html/app/vendor/ciscn/fm && \
    chmod 0755 /flag && \
    chown -R www-data:www-data /var/www/html/app/storage

CMD "/entrypoint"

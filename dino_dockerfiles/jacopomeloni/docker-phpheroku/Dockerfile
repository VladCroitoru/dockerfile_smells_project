FROM php:7.2-fpm-alpine

LABEL MANTAINER=jacopomeloni@gmail.com

# install packages
RUN apk --update add \
    nginx \
    supervisor \
    gettext libintl \
    && mv /usr/bin/envsubst /usr/local/sbin/envsubst \
    && rm -rf /var/cache/apk/* \
    && rm -rf /var/www/html \
    && mkdir -p /var/log/supervisord

# set the nginx configuration
COPY ./conf/nginx/default.conf /default.conf
COPY ./conf/nginx/nginx.conf /etc/nginx/nginx.conf

# copy the phpfpm configuration
COPY ./conf/phpfpm/php-fpm.conf /usr/local/etc/php-fpm.conf
COPY ./conf/phpfpm/www.conf /usr/local/etc/php-fpm.d/www.conf

# copy the supervisord configuration
ADD ./conf/supervisord/supervisor.ini /etc/supervisor.d/supervisor.ini

# copy the start scripts
COPY ./conf/scripts/startNginx.sh /startNginx.sh
COPY ./conf/scripts/startPhpFpm.sh /startPhpFpm.sh
RUN chmod +x /startNginx.sh && \
    chmod +x /startPhpFpm.sh

# copy the application code
COPY ./public/ /var/www/public

WORKDIR /var/www

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.d/supervisor.ini"]
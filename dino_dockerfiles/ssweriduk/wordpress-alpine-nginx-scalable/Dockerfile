FROM wordpress:php7.1-fpm-alpine
MAINTAINER Stephen Sweriduk <ssweriduk@gmail.com>

#Add nginx and supervisor
RUN apk add --no-cache nginx supervisor

#Configure external wp-content folder
COPY wp-config.php /usr/src/wordpress
RUN chown -R www-data:www-data /usr/src/wordpress \
    && chmod 640 /usr/src/wordpress/wp-config.php

VOLUME /var/www/wp-content

#Wordpress wp-content files & directories
COPY entrypoint.sh /usr/local/bin/
ENTRYPOINT [ "entrypoint.sh" ]

#NGINX config
COPY nginx.conf /etc/nginx/nginx.conf
COPY vhost.conf /etc/nginx/conf.d/
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && chown -R www-data:www-data /var/lib/nginx

#PHP Production config
COPY php.ini /usr/local/etc/php/conf.d/

#Supervisor config
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisord.conf
COPY stop-supervisor.sh /usr/local/bin/

CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisord.conf" ]

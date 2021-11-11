FROM wordpress:php7.1-fpm-alpine
MAINTAINER Philip G <gp@gpcentre.net>

RUN apk add --update --no-cache nginx supervisor 

# Debug tools. Comment out for "official" push
#RUN apk add --no-cache wget curl vim bash mysql-client
#RUN echo 'alias ls="ls --color=auto"' >> ~/.bashrc
#RUN echo 'alias ll="ls --color=auto -l"' >> ~/.bashrc

ENV HOME /root
ENV TERM xterm
ENV WP_ROOT  /usr/src/wordpress

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && chown -R www-data:www-data /var/lib/nginx

VOLUME ["/var/lib/php-fpm/"]
WORKDIR /var/www/wp-content

RUN mkdir -p /var/log/supervisor
COPY etc/supervisord.conf /etc/supervisord.conf
COPY stop-supervisor.sh /usr/local/bin/

# on wp-config to rule them all. Set values in .env file
COPY wp-config.php $WP_ROOT
RUN chown -R www-data:www-data $WP_ROOT \
   && chmod 640 $WP_ROOT/wp-config.php

RUN chgrp -R www-data /var/www/wp-content \
   && chmod -R g+ws /var/www/wp-content  \
   # This fixes an issue with php-fpm uploads unable to see nginx uploaded files
   && chmod g+rX /var/lib/nginx/tmp

COPY ./etc/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./etc/php-fpm/php-fpm.d/zz-docker.conf /usr/local/etc/php-fpm.d/zz-docker.conf
COPY ./etc/php-fpm/conf.d/zz-docker.ini /usr/local/etc/php/conf.d/zz-docker.ini

# Allows the ability to run / monitor two processes on startup
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisord.conf" ]

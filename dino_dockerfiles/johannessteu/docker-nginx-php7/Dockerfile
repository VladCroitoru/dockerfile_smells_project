FROM ubuntu:16.04
MAINTAINER Johannes Steu <js@johannessteu.de>

RUN apt-get update && apt-get install -y php php-fpm nginx supervisor bash vim

RUN mkdir -p /data/www/vhost \
    && mkdir -p /data/logs \
    && mkdir -p /data/tmp/nginx \
    && mkdir -p /data/tmp/php \
    && mkdir -p /data/tmp/php/uploads \
    && mkdir -p /data/tmp/php/sessions \
    && mkdir -p /var/run/

RUN rm -rf /etc/nginx/*.d /etc/nginx/*_params

RUN rm -rf /tmp/*
RUN chown -R www-data:www-data /data/www
RUN usermod -d /data/www -s /bin/bash www-data
ADD /container-files/etc /etc

EXPOSE 80 443

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
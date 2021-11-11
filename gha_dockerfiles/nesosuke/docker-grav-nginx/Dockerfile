FROM ubuntu:focal
USER root
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get -y install \
        unzip g++ git vim cron wget \
        php7.4 \
        php7.4-curl \
        php7.4-gd \
        php7.4-fpm \
        php7.4-json \
        php7.4-mbstring \
        php7.4-xml \
        php7.4-zip \
        nginx 
COPY webserver-conf/grav.conf /etc/nginx/sites-enabled/

RUN chown -R www-data:www-data /var/www 

USER www-data 
WORKDIR /var/www
RUN wget https://getgrav.org/download/core/grav-admin/latest -O grav-latest.zip \
    && unzip grav-latest.zip \
    && mv grav-admin /var/www/grav \ 
    && rm grav-latest.zip

USER root
CMD ["sh", "-c", "service php7.4-fpm restart && /usr/sbin/nginx -g 'daemon off;'"]
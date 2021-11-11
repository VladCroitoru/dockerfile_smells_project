FROM nginx
MAINTAINER francoisp

ENV LANG C.UTF-8

RUN apt-get update; apt-get install -y \
    openssl \
    wget \
    postgresql-client \
    php5-intl \
    php5-mcrypt \
    php5-mysql \
    php5-pgsql \
    mysql-client \ 
    php5-fpm

RUN rm -rf /etc/nginx/conf.d/*; \
    mkdir -p /etc/nginx/external

RUN sed -i 's/access_log.*/access_log \/dev\/stdout;/g' /etc/nginx/nginx.conf; \
    sed -i 's/error_log.*/error_log \/dev\/stdout info;/g' /etc/nginx/nginx.conf; \
    sed -i 's/^pid/daemon off;\npid/g' /etc/nginx/nginx.conf

ADD basic.conf /etc/nginx/conf.d/basic.conf
ADD ssl.conf /etc/nginx/conf.d/ssl.conf

ADD entrypoint.sh /opt/entrypoint.sh
RUN chmod a+x /opt/entrypoint.sh


# fix pathinfo see: (https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-on-ubuntu-14-04)
RUN sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php5/fpm/php.ini

# enable php5 mcrypt
RUN php5enmod mcrypt

# install roundcube
RUN wget "http://sourceforge.net/projects/roundcubemail/files/latest/download" -O roundcubemail.tar.gz && \
    tar xvf roundcubemail.tar.gz -C / && \
    rm roundcubemail.tar.gz; \
    mv /roundcube* /roundcube

# fix rights
RUN chmod a+rw /roundcube/temp/; \
    chmod a+rw /roundcube/logs/

# add config
ADD config.inc.php /roundcube/config/config.inc.php

# install nginx roundcube config
ADD nginx-roundcube.conf /etc/nginx/conf.d/nginx-roundcube.conf

# add startup.sh
ADD startup-roundcube.sh /opt/startup-roundcube.sh
RUN chmod a+x /opt/startup-roundcube.sh

ENTRYPOINT ["/opt/entrypoint.sh"]
CMD ["nginx"]

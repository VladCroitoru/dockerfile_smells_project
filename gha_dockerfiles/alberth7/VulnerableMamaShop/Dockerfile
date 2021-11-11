From ubuntu:xenial

RUN apt-get update && \
    apt-get install -y \
    apache2 \
    libapache2-mod-fastcgi \
    php7.0-fpm \
    mariadb-server \
    php-mysql \
    gosu &&\
    a2dismod -f deflate &&\
    a2enmod proxy proxy_fcgi

COPY 000-default.conf /etc/apache2/sites-enabled
COPY init /root/

RUN mkdir dmonitor &&\
    chmod 755 dmonitor 
    
COPY init/mon.sh /dmonitor

COPY apps /var/www/html

RUN chmod 755 /dmonitor/mon.sh &&\
    chmod 644 /var/www/html/*

EXPOSE 80/tcp

#CMD ["/bin/bash" , "-i"]
ENTRYPOINT ["/bin/bash", "/root/start.sh"]

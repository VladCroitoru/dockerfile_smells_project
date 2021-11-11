FROM php:5.6-apache

RUN apt-get update &&\
    apt-get -y install runit libsnmp-dev snmp rrdtool mysql-client &&\
    docker-php-ext-install -j$(nproc) mysql snmp sockets &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL http://www.cacti.net/downloads/cacti-0.8.8h.tar.gz |\
    tar xvzf - --strip-components=1 --directory=/var/www/html/

RUN curl -fsSL https://github.com/michaloo/go-cron/releases/download/v0.0.2/go-cron.tar.gz |\
    tar xvf - --directory=/usr/local/bin

COPY ./files/config.php       /var/www/html/include/
COPY ./files/cacti-startup.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/cacti-startup.sh

VOLUME /var/www/html/log
VOLUME /var/www/html/rra

EXPOSE 80
ENV MYSQL_PORT 3306
CMD [ "cacti-startup.sh" ]

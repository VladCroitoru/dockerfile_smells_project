# Version 0.0.2
FROM whooshkaa/php7-laravel
MAINTAINER Phil Dodd "phil@whooshkaa.com"
ENV LAST_UPDATED 2017-05-18

ENV DEBIAN_FRONTEND noninteractive

# Adding the official Oracle MySQL APT repositories to install MySQL 5.6 (including the apt-get key)
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 5072E1F5
RUN echo "deb http://repo.mysql.com/apt/debian/ jessie mysql-5.6" >> /etc/apt/sources.list

# mysql
RUN apt-get update -y
RUN apt-get install -y mysql-client mysql-server python-mysqldb

# copy supervisor file with added mysql start command
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# setup mysql
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf
ADD set-mysql-password.sh /tmp/set-mysql-password.sh
RUN /bin/sh /tmp/set-mysql-password.sh

EXPOSE 80
CMD ["/usr/bin/supervisord"]


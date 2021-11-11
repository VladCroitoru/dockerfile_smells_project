FROM whooshkaa/docker-php:latest
MAINTAINER Phil Dodd "phil@whooshkaa.com"
ENV LAST_UPDATED 2019-12-19

# mysql
RUN apt-get update && apt-get install -y mysql-client mysql-server python-mysqldb

#Create directories for lock files
RUN  mkdir -p /var/run/mysqld
RUN chmod -R a+w /var/run/mysqld

# copy supervisor file with added mysql start command
RUN rm /etc/supervisor/conf.d/supervisord.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# setup mysql
#RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf
ADD set-mysql-password.sh /tmp/set-mysql-password.sh
#RUN /bin/sh /tmp/set-mysql-password.sh
RUN echo 'sql-mode="NO_ENGINE_SUBSTITUTION"' >>  /etc/mysql/mysql.conf.d/mysqld.cnf
# Allow remote connections (for the api app)
RUN sed -i -e 's/bind-address/#bind-address/g' /etc/mysql/mysql.conf.d/mysqld.cnf
RUN /bin/sh /tmp/set-mysql-password.sh

EXPOSE 80
CMD ["/usr/bin/supervisord"]



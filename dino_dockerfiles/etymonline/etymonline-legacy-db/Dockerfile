FROM ubuntu:12.04
MAINTAINER Drew Carey Buglione <drew@etymonline.com>

RUN apt-get -y install mysql-server
RUN sed -i -e s/"127.0.0.1"/"0.0.0.0"/ /etc/mysql/my.cnf

EXPOSE 3306
CMD ["/usr/sbin/mysqld"]

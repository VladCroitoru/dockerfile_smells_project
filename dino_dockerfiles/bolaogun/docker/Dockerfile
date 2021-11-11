FROM ubuntu:latest
MAINTAINER A. Bravo <a@b.com>
#RUN debconf-set-selections <<< 'mysql-server mysql-server/root_password password pass'
#RUN debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password pass'
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y mysql-server
ENV TERM vt100
ENV username mysqlserver
ENV password pass
ENV database db2
ADD databasesetup.sh /
RUN chmod 755 /databasesetup.sh
RUN "/databasesetup.sh"
EXPOSE 3306
CMD ["/usr/bin/mysqld_safe"]

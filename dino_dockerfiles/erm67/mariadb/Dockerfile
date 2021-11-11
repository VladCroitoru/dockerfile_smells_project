FROM fedora:22
MAINTAINER Ermanno Scaglione <erm67@yahoo.it>
RUN dnf -y update && dnf -y install mariadb-server hostname && dnf clean all
ADD mariadb-server.cnf /etc/my.cnf.d/mariadb-server.cnf
EXPOSE 3306
# ENV MYSQL_ROOT_PASSWORD
# ENV MYSQL_ALLOW_EMPTY_PASSWORD true
# ENV MYSQL_USER
# ENV MYSQL_PASSWORD
# ENV MYSQL_DATABASE

COPY docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh
USER mysql
VOLUME ["/var/run/mariadb/"]
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["mysqld"]

FROM mysql:5.6

MAINTAINER Teerapong Kriamornchai <teerapong@maqe.com>

RUN sed -e "s/\,\?STRICT_TRANS_TABLES\,\?//" -i /etc/mysql/my.cnf
RUN mkdir -p /var/lib/db
RUN sed -i 's/\/var\/lib\/mysql/\/var\/lib\/db/g' /entrypoint.sh
CMD ["mysqld", "--datadir=/var/lib/db", "--user=mysql", "--skip-name-resolve"]
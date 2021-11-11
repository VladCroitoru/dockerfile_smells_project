FROM mysql:5.6.36

ENV MYSQL_DATABASE=sse

ADD ./my-custom.cnf /etc/mysql/mysql.conf.d/my-custom.cnf
ADD schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306
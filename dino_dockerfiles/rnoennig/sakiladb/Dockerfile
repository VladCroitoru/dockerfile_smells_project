FROM mariadb

RUN apt-get update && apt-get install -y --no-install-recommends wget

RUN wget http://downloads.mysql.com/docs/sakila-db.tar.gz
RUN tar xaf sakila-db.tar.gz

RUN cp sakila-db/sakila-schema.sql /docker-entrypoint-initdb.d/01_sakila_schema.sql
RUN cp sakila-db/sakila-data.sql /docker-entrypoint-initdb.d/02_sakila_data.sql

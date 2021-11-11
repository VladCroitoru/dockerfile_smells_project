FROM mdillon/postgis:10-alpine
ADD gost_init_db.sql /docker-entrypoint-initdb.d/
ADD entry.sh /docker-entrypoint-initdb.d/
ADD postgresql.conf /etc/postgresql/conf/postgresql.conf
RUN chmod 777 /etc/postgresql/conf/postgresql.conf

FROM postgres:12

RUN mkdir -p /var/lib/postgresql-static/data
ENV PGDATA /var/lib/postgresql-static/data

RUN apt-get update
RUN apt-get install wget unzip -y

ARG DUMP_URI=https://edu.postgrespro.ru/demo-small.zip
RUN wget --output-document=dbdump.zip $DUMP_URI
RUN unzip dbdump.zip -d dbdump


RUN echo "" > /docker-entrypoint-initdb.d/run_dbdump.sh
RUN echo "psql -t template1 -U postgres -c 'alter system set shared_preload_libraries=''pg_stat_statements'',''pg_buffercache'';'" >> /docker-entrypoint-initdb.d/run_dbdump.sh
RUN echo "psql -U postgres -f /dbdump/demo-small-20170815.sql" >> /docker-entrypoint-initdb.d/run_dbdump.sh

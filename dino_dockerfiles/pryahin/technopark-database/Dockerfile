FROM ubuntu:16.04

MAINTAINER Pryahin Vladimir

# Обвновление списка пакетов
RUN apt-get -y update

#
# Установка postgresql
#
ENV PGVER 9.5
RUN apt-get update
RUN apt-get install -y postgresql-$PGVER

# Run the rest of the commands as the ``postgres`` author created by the ``postgres-$PGVER`` package when it was ``apt-get installed``
USER postgres

# Create a PostgreSQL role named ``docker`` with ``docker`` as the password and
# then create a database `docker` owned by the ``docker`` role.
RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
    createdb -E UTF8 -T template0 -O docker docker &&\
    /etc/init.d/postgresql stop

    
# Adjust PostgreSQL configuration so that remote connections to the
# database are possible.
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/$PGVER/main/pg_hba.conf

# And add ``listen_addresses`` to ``/etc/postgresql/$PGVER/main/postgresql.conf``
RUN echo "listen_addresses='*'" >> /etc/postgresql/$PGVER/main/postgresql.conf
RUN echo "synchronous_commit = off" >> /etc/postgresql/$PGVER/main/postgresql.conf
RUN echo "shared_buffers = 256MB" >> /etc/postgresql/$PGVER/main/postgresql.conf
RUN echo "autovacuum = off" >> /etc/postgresql/$PGVER/main/postgresql.conf


# Expose the PostgreSQL port
EXPOSE 5432

# Add VOLUMEs to allow backup of application.config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# Back to the root author
USER root

##
 # Сборка проекта
 #

 # Установка JDK

RUN apt-get update
RUN apt-get install -y openjdk-8-jdk-headless

RUN apt-get install -y maven

# Копируем исходный код в Docker-контейнер

ENV WORK /opt/BDServer
ADD src/ $WORK/src/
ADD pom.xml $WORK/

# Собираем и устанавливаем пакет

WORKDIR $WORK
# RUN rm -rf target/
RUN mvn package

# Объявлем порт сервера
EXPOSE 5000

CMD service postgresql start && java -jar target/Database-1.0-SNAPSHOT.jar application.Application 

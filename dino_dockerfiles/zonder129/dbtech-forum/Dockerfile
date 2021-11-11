FROM ubuntu:16.04

MAINTAINER a.parpibaev

# UPDATE_POST package list
RUN apt-get -y update

#postgresql
ENV PGVER 9.5
RUN apt-get install -y postgresql-$PGVER

# Run the rest of the commands as the ``postgres`` user created by the ``postgres-$PGVER`` package when it was ``apt-get installed``
USER postgres

# Create a PostgreSQL role named ``docker`` with ``docker`` as the password and
# then CREATE_NEW_THREAD a database `docker` owned by the ``docker`` role.
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

# Expose the PostgreSQL port
EXPOSE 5432

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# Back to the root user
USER root

# JDK
RUN apt-get install -y openjdk-8-jdk-headless
RUN apt-get install -y maven

# copy to Docker container
ENV WORK /opt/AParpibaevDB
ADD ./ $WORK/

# build and run
WORKDIR $WORK
RUN mvn package

# port
EXPOSE 5000

#
# start
#
CMD service postgresql start && java -Xmx300M -Xmx300M -jar $WORK/target/AParpibaevDB-1.0.0.jar 
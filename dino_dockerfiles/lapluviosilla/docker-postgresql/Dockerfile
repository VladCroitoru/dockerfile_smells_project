# Postgresql (http://www.postgresql.org/)

FROM ubuntu:12.04
MAINTAINER Ryan Seto <ryanseto@yak.net>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list

# Ensure UTF-8
RUN apt-get update
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8

# Get the Postgresql keys
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget
RUN wget --quiet --no-check-certificate -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

# Install the latest postgresql
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes postgresql-9.2 postgresql-client-9.2 postgresql-contrib-9.2 && \
    /etc/init.d/postgresql stop

# Install other tools.
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y pwgen inotify-tools

RUN mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-copy/; rm -r /etc/ssl/private; mv /etc/ssl/private-copy /etc/ssl/private; chmod -R 0700 /etc/ssl/private; chown -R postgres /etc/ssl/private

# Decouple our data from our container.
VOLUME ["/data", "/var/log/postgresql"]

RUN echo "Dropping current cluster" && \
    pg_dropcluster --stop 9.2 main

RUN echo "Creating new cluster with UTF8 encoding" && \
    pg_createcluster --locale=en_US.UTF8 --start 9.2 main

# Cofigure the database to use our data dir.
RUN sed -i -e"s/data_directory =.*$/data_directory = '\/data'/" /etc/postgresql/9.2/main/postgresql.conf
# Allow connections from anywhere.
RUN sed -i -e"s/^#listen_addresses =.*$/listen_addresses = '*'/" /etc/postgresql/9.2/main/postgresql.conf
RUN echo "host    all    all    0.0.0.0/0    md5" >> /etc/postgresql/9.2/main/pg_hba.conf

EXPOSE 5432
ADD scripts /scripts
RUN chmod +x /scripts/start.sh
RUN touch /firstrun

ENTRYPOINT ["/scripts/start.sh"]

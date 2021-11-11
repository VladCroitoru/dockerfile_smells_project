#######################################################
# PostgreSQL database instance. Supports the Rolltime
# collector and forecasting services.
#######################################################

FROM ubuntu:14.04

#
# Fetch PostgreSQL PGP key.
#
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

#
# Add official PostgreSQL repo.
#
RUN \
  echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main 9.5" > /etc/apt/sources.list.d/pgdg.list

# Install ``python-software-properties``, ``software-properties-common`` and PostgreSQL 9.5
#  There are some warnings (in red) that show up during the build. You can hide
#  them by prefixing each apt-get statement with DEBIAN_FRONTEND=noninteractive
RUN \
  apt-get update \
  && apt-get install -y python-software-properties software-properties-common \
    postgresql-9.5 postgresql-client-9.5 postgresql-contrib-9.5

#
# The rest of the commands have
# to be run as the `postgres` user
# for default security reasons.
#
USER postgres

#
# Create Rolltime db user with password.
#
RUN /etc/init.d/postgresql start \
    && psql --command "CREATE USER metabase WITH SUPERUSER PASSWORD 'metabase';" \
    && createdb -O metabase metabase

#
# Allow remote connections.
#
USER root
RUN \
  echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.5/main/pg_hba.conf \
  && echo "listen_addresses='*'" >> /etc/postgresql/9.5/main/postgresql.conf

EXPOSE 5432

#
# Volumes for configuration files, logs,
# and databases to be mapped to host.
#
RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

#
# Starts database.
#
USER postgres
CMD ["/usr/lib/postgresql/9.5/bin/postgres", "-D", "/var/lib/postgresql/9.5/main", "-c", "config_file=/etc/postgresql/9.5/main/postgresql.conf"]

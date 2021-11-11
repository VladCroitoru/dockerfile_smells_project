FROM ubuntu:precise
MAINTAINER Brian Olsen "brian@maven-group.org"

# Add dokdb script
ADD https://github.com/griff/dokdb/raw/master/src/common.bash /usr/local/share/dokdb/
RUN chmod 755 /usr/local/share/dokdb/common.bash

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -q -y curl sudo bsdmainutils socat

# Add Postgres apt repository
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main' > /etc/apt/sources.list.d/pgdg.list
RUN curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -q -y postgresql-common postgresql-client-9.3

# prevent apt from creating cluster and starting postgres right after the installation
RUN echo "create_main_cluster = false\nstart_conf = 'manual'" >> /etc/postgresql-common/createcluster.conf

RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y postgresql-9.3 postgresql-contrib-9.3

# Create directory so that pg_createcluster can be run as postgres user
RUN mkdir -p /var/lib/postgresql/etc
RUN chown -R postgres:postgres /var/lib/postgresql/etc
RUN ln -sf /var/lib/postgresql/etc /etc/postgresql

ENV DATABASE_SCHEME postgresql
ENV DATABASE_NAME demo
ENV DATABASE_USER demo
ENV DATABASE_PASSWORD demo
ENV DATABASE_ADMIN_USER admin
ENV DATABASE_ADMIN_PASSWORD admin
ENV DATABASE_PORT 5432
ENV DATABASE_LOCALE en_US.UTF-8
ENV DATABASE_EXTENSIONS optional
ENV DATABASE_SERVER_ONLY false

# Generate the default locale
RUN locale-gen en_US.UTF-8

# Add launch script
ADD launch.bash /launch

ADD own-volume.sh /usr/local/bin/own-volume
RUN echo "postgres ALL=NOPASSWD: /usr/local/bin/own-volume, /usr/sbin/locale-gen" >> /etc/sudoers

VOLUME ["/var/lib/postgresql"]
EXPOSE 5432
USER postgres
ENTRYPOINT ["/launch"]
CMD ["run"]
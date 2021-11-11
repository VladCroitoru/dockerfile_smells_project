#
# OsmPostgres
# Image containing PostgreSQL server and a database prepared to be used for OSM data.
#

FROM mytracks/osmbase:latest
MAINTAINER "Dirk Stichling" <mytracks@mytracks4mac.com>

# Install postgres
RUN rpm -ivh http://yum.postgresql.org/9.5/redhat/rhel-7-x86_64/pgdg-centos95-9.5-2.noarch.rpm \
&& yum -y install epel-release \
&& yum -y install postgresql95-server postgis2_95

COPY osm2pgsql-1.0.0-1.el7.centos.x86_64.rpm /tmp/

RUN yum -y install boost proj-epsg

RUN rpm -Uvh /tmp/osm2pgsql-1.0.0-1.el7.centos.x86_64.rpm \
&& rm /tmp/*.rpm

# Create Postgres data directory
RUN mkdir /home/pgdata; chown postgres.postgres /home/pgdata

#
# Postgres
#

USER postgres

RUN /usr/pgsql-9.5/bin/pg_ctl -D /home/pgdata/osm initdb

RUN echo host gis gis 0.0.0.0/0 trust >> /home/pgdata/osm/pg_hba.conf \
&& echo local all all trust >> /home/pgdata/osm/pg_hba.conf \
&& sed -i.bak "s/#\?listen_addresses \?=.*/listen_addresses = '*'/g" /home/pgdata/osm/postgresql.conf \
&& sed -i.bak "s/#\?port \?=.*/port = 5432/g" /home/pgdata/osm/postgresql.conf \
&& sed -i.bak 's/#\?silent_mode \?=.*/silent_mode = on/g' /home/pgdata/osm/postgresql.conf \
&& sed -i.bak 's/#\?shared_buffers \?=.*/shared_buffers = 512kB/g' /home/pgdata/osm/postgresql.conf \
&& sed -i.bak 's/#\?work_mem \?=.*/work_mem = 1GB/g' /home/pgdata/osm/postgresql.conf \
&& sed -i.bak 's/#\?maintenance_work_mem \?=.*/maintenance_work_mem = 1GB/g' /home/pgdata/osm/postgresql.conf \
&& sed -i.bak 's/#\?wal_level \?=.*/wal_level = minimal/g' /home/pgdata/osm/postgresql.conf \
&& sed -i.bak 's/#\?fsync \?=.*/fsync = on/g' /home/pgdata/osm/postgresql.conf \
&& sed -i.bak 's/#\?synchronous_commit \?=.*/synchronous_commit = off/g' /home/pgdata/osm/postgresql.conf \
&& sed -i.bak 's/#\?checkpoint_segments \?=.*/checkpoint_segments = 64/g' /home/pgdata/osm/postgresql.conf \
&& sed -i.bak 's/#\?checkpoint_timeout \?=.*/checkpoint_timeout = 15min/g' /home/pgdata/osm/postgresql.conf \
&& sed -i.bak 's/#\?checkpoint_completion_target \?=.*/checkpoint_completion_target = 0.9/g' /home/pgdata/osm/postgresql.conf \
&& sed -i.bak 's/#\?default_statistics_target \?=.*/default_statistics_target = 1000/g' /home/pgdata/osm/postgresql.conf \
&& sed -i.bak 's/#\?autovacuum \?=.*/autovacuum = off/g' /home/pgdata/osm/postgresql.conf

RUN /usr/pgsql-9.5/bin/pg_ctl -D /home/pgdata/osm start \
&& sleep 5 \
&& createuser gis \
&& createdb --template=template0 -E UTF8 -O gis gis \
&& psql -d gis -c "CREATE EXTENSION postgis;" \
&& echo "ALTER TABLE geometry_columns OWNER TO gis; ALTER TABLE spatial_ref_sys OWNER TO gis;"  | psql -d gis \
&& /usr/pgsql-9.5/bin/pg_ctl -D /home/pgdata/osm stop

#
# osm2pgsql
#

USER root

# Clean up
RUN yum clean all

# Expose the PostgreSQL port
EXPOSE 5432

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/home/pgdata"]

COPY start.sh /etc/

# Set the default command to run when starting the container
ENTRYPOINT ["/etc/start.sh"]


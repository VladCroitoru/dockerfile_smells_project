FROM postgres:9.6

MAINTAINER Sylvain Caillet (s.caillet@free.fr)

RUN apt-get update && apt-get install -y \
    git \
    libpq-dev \
    libprotobuf-c0-dev \
    make \
    postgresql-server-dev-9.6 \
    protobuf-c-compiler \
    gcc

RUN cd /tmp && git clone -b v1.6.0 https://github.com/citusdata/cstore_fdw.git

RUN cd /tmp/cstore_fdw && PATH=/usr/local/pgsql/bin/:$PATH make && PATH=/usr/local/pgsql/bin/:$PATH make install

RUN cp /usr/share/postgresql/postgresql.conf.sample /etc/postgresql/postgresql.conf
RUN sed -i "s/#shared_preload_libraries = ''/shared_preload_libraries = 'cstore_fdw'/g" /etc/postgresql/postgresql.conf





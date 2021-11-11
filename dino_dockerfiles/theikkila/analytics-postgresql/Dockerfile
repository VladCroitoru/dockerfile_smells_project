FROM postgres:10

RUN apt-get update && apt-get install -y protobuf-c-compiler libprotobuf-c0-dev wget make postgresql-server-dev-10 build-essential
RUN wget https://github.com/citusdata/postgresql-hll/archive/v2.10.2.tar.gz -O /tmp/hll.tar.gz && cd /tmp && tar -xzvf hll.tar.gz
RUN cd /tmp/postgresql-hll-2.10.2 && make && make install

RUN wget https://github.com/citusdata/cstore_fdw/archive/v1.6.0.tar.gz -O /tmp/cstore.tar.gz && cd /tmp && tar -xzvf cstore.tar.gz
RUN cd /tmp/cstore_fdw-1.6.0 && make && make install

RUN echo "shared_preload_libraries = 'cstore_fdw'" >> /usr/share/postgresql/postgresql.conf.sample

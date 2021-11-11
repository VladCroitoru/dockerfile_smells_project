# Azurewind's PostgreSQL image with Chinese full text searchi using pg_jieba

FROM postgres:alpine

RUN apk add --no-cache --virtual .build \
        postgresql-dev \
        gcc \
        make \
        llvm \
        libc-dev \
        g++ \
        clang \
        git \
        cmake \
        curl \
        openssl-dev && \
    git clone https://github.com/jaiminpan/pg_jieba && \
    cd /pg_jieba && \
    git submodule update --init --recursive && \
    mkdir -p build && \
    cd build && \
    curl -L https://raw.githubusercontent.com/ssfdust/psql_jieba_swsc/master/FindPostgreSQL.cmake > $(find /usr -name "FindPostgreSQL.cmake") && \
    cmake .. && \
    make && \
    make install && \
    cd / && \
    git clone https://github.com/jaiminpan/pg_scws && \
    cd /pg_scws && \
    USE_PGXS=1 make && \
    USE_PGXS=1 make install && \
    apk del .build && \
    rm -rf /pg_jieba /pg_scws

RUN echo "echo \"shared_preload_libraries = 'pg_jieba'\" >> /var/lib/postgresql/data/postgresql.conf" \
    > /docker-entrypoint-initdb.d/init-dict.sh  && \
    echo "CREATE EXTENSION pg_jieba;create extension pg_scws;" > /docker-entrypoint-initdb.d/init-jieba.sql

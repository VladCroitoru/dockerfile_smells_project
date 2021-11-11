FROM alpine:3.1
MAINTAINER Petr Orlov <zfmeze@gmail.com>

RUN    apk add --update libstdc++ readline libgomp \
                        binutils-libs libpq curl-dev icu-dev \
    && apk add --update  --virtual .tarantool-deps \
            git cmake g++ make readline-dev perl postgresql-dev \
    && git clone https://github.com/tarantool/tarantool.git /tarantool \
    && git clone https://github.com/tarantool/pg.git /tarantool-pq \
    && cd /tarantool && git submodule update --init --recursive \
    && cmake -DCMAKE_BUILD_TYPE=Release . && make && make install \
    && cd /tarantool-pq && git submodule update --init --recursive \
    && cmake -DCMAKE_BUILD_TYPE=Release . && make && make install \
    && apk del .tarantool-deps \
    && rm /var/cache/apk/* \
    && rm -rf /tarantool* \
    && mkdir /data


ENV TRT_PORT 3301
ENV TRT_USER root
ENV TRT_PASS password

EXPOSE 3301

VOLUME ["/data"]

COPY ["./run.sh", "/run.sh"]

ENTRYPOINT ["/run.sh"]

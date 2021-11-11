FROM alpine:3.7
MAINTAINER JS Minet
ARG REPOSITORY=https://github.com/tpruvot/yiimp.git

ENV BUILD_DEPS \
 build-base \
 curl-dev \
 git \
 gmp-dev \
 iniparser \
 mariadb-dev \ 
 libssh2-dev

RUN apk update \
 && apk add --no-cache ${BUILD_DEPS} \   
 && git clone --progress ${REPOSITORY} ~/yiimp \
 && make -C ~/yiimp/stratum/iniparser \
 && make -C ~/yiimp/stratum \
 && mkdir /var/stratum /var/stratum/config \
 && cp ~/yiimp/stratum/run.sh /var/stratum \
 && cp ~/yiimp/stratum/config/run.sh /var/stratum/config \
 && cp ~/yiimp/stratum/stratum /var/stratum \
 && cp ~/yiimp/stratum/config.sample/neo.conf /var/stratum/config \
 && rm -rf ~/yiimp \
 && apk del ${BUILD_DEPS} \
 && rm -rf /var/cache/apk/*
 
RUN apk add --no-cache bash

WORKDIR /var/stratum

CMD ["bash", "run.sh", "neo.conf"]

EXPOSE 4233
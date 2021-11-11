FROM mysql:5.7.21
MAINTAINER JS Minet
ARG REPOSITORY=https://github.com/tpruvot/yiimp.git

ENV BUILD_DEPS \
 ca-certificates \
 git

COPY init-db.sh /docker-entrypoint-initdb.d/

RUN apt-get update \
 && apt-get install -y --no-install-recommends ${BUILD_DEPS} \
 && git clone --progress ${REPOSITORY} ~/yiimp \
 && mkdir /tmp/sql \
 && mv ~/yiimp/sql/2016-04-03-yaamp.sql.gz /tmp/sql/0000-00-00-initial.sql.gz \
 && cp ~/yiimp/sql/*.sql /tmp/sql \
 && apt-get purge -y --auto-remove ${BUILD_DEPS} \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf ~/yiimp
  
EXPOSE 3306
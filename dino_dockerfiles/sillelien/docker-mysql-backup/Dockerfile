FROM sillelien/jessie
MAINTAINER Neil Ellis <hello@neilellis.me>

ENV DEBIAN_FRONTEND noninteractive
ENV MYSQL_HOST 127.0.0.1
ENV MYSQL_PORT 3306
ENV MYSQL_USER root
ENV RESTORE_DB_CHARSET utf8
ENV RESTORE_DB_COLLATION utf8_bin
ENV S3_PATH mysql

RUN apt-get update \
    && apt-get install -yq --no-install-recommends python-pip mysql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* \
    && pip install awscli

ADD start.sh /start.sh

ENTRYPOINT  ["/init","/start.sh"]

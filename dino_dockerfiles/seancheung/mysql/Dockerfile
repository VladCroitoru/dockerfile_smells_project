FROM ubuntu:16.04
LABEL maintainer="Sean Cheung <theoxuanx@gmail.com>"

RUN set -x \
    && apt-get update \
    && export DEBIAN_FRONTEND="noninteractive" \
    && apt-get install -y --no-install-recommends mysql-server mysql-client \
    && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh
COPY my.cnf /etc/mysql/my.cnf

VOLUME ["/var/lib/mysql"]
EXPOSE 3306

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/usr/sbin/mysqld"]

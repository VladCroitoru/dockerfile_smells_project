FROM alpine:latest

ENV LC_ALL=en_US.UTF-8

RUN mkdir /docker-entrypoint-initdb.d && \
    apk -U upgrade && \
    apk add --no-cache mariadb mariadb-client && \
    apk add --no-cache tzdata && \
    # clean up
    rm -rf /var/cache/apk/*

# comment out a few problematic configuration values
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf && \
    # don't reverse lookup hostnames, they are usually another container
    sed -i '/^\[mysqld]$/a skip-host-cache\nskip-name-resolve' /etc/mysql/my.cnf && \
    # always run as user mysql
    sed -i '/^\[mysqld]$/a user=mysql' /etc/mysql/my.cnf

VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 3306

# Default arguments passed to ENTRYPOINT if no arguments are passed when starting container
CMD ["mysqld_safe"]

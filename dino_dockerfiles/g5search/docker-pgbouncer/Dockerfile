FROM debian:jessie
MAINTAINER G5 Devops <devops@getg5.com>

RUN set -x && \
    apt-get -qq update && \
    apt-get install -yq --no-install-recommends pgbouncer gettext && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 6432

ENV LISTEN_ADDR="0.0.0.0" \
    LISTEN_PORT="6432" \
    POOL_MODE="transaction"  \
    MAX_CLIENT_CONN="20" \
    DEFAULT_POOL_SIZE="20" \
    CLIENT_DBNAME="foo" \
    CLIENT_USER="bar" \
    CLIENT_PASSSWORD="password" \
    STATS_USER="baz" \
    STATS_PASSWORD="password" \
    SERVER_HOST="127.0.0.1" \
    SERVER_PORT="5432" \
    SERVER_DBNAME="foo" \
    SERVER_USER="bar" \
    SERVER_PASSWORD="password"

ADD pgbouncer.template.ini /
ADD start.sh /

# it refuses to run as root, scoffs if there is no /etc/passwd entry for the
# user you run it as, and must be able to write its own config file from the
# template
RUN groupadd -r pgbouncer && \
    useradd -r -g pgbouncer pgbouncer && \
    chown -R pgbouncer /etc/pgbouncer && \
    mkdir /var/run/pgbouncer && \
    chown -R pgbouncer /var/run/pgbouncer
USER pgbouncer

CMD [ "./start.sh" ]

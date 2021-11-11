FROM qnib/alplain-init

ENV PGDATA=/var/lib/pgsql/data/ \
    ENTRY_USER=postgres \
    PSQL_BIND_ADDR=*
RUN apk add --update postgresql \
 && mkdir -p /var/lib/pgsql/data/ \
 && chown postgres: /var/lib/pgsql/data \
 && su -l -c "pg_ctl -c initdb -D /var/lib/pgsql/data/" postgres
COPY var/lib/pgsql/data/pg_hba.conf /var/lib/pgsql/data/
COPY opt/qnib/entry/20-psql-config.sh /opt/qnib/entry/
COPY opt/qnib/pgsql/etc/postgresql.conf /opt/qnib/pgsql/etc/
CMD ["/usr/bin/postgres", "-D", "/var/lib/pgsql/data"]

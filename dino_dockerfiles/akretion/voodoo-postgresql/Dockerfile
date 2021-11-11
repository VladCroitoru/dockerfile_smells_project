FROM postgres:10.3
MAINTAINER sebastien.beau@akretion.com

RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y postgresql-contrib && \
    apt-get clean

COPY dev-docker-entrypoint.sh /
COPY initdb.sh /docker-entrypoint-initdb.d/initdb.sh
COPY postgresql.conf /etc/postgresql/postgresql.conf
RUN chown postgres:postgres /etc/postgresql/postgresql.conf
ENTRYPOINT ["/dev-docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]

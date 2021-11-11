FROM ubuntu
MAINTAINER Mario Mainz

# install postgres
RUN apt-get update
RUN apt-get install -y postgresql postgresql-contrib

# adjust PostgreSQL configuration so that remote connections to the database are possible
RUN echo "host all  all    0.0.0.0/0  trust" >> /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

USER postgres

COPY adjust-encoding.sh adjust-encoding.sh
RUN ./adjust-encoding.sh

EXPOSE 5432

CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]

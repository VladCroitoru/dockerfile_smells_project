FROM ubuntu:trusty
MAINTAINER el aras<openmason@gmail.com>

# Credentials
ENV USERNAME docker
ENV PASS d0cker

RUN apt-get -yq update
RUN apt-get -yq install wget ca-certificates --no-install-recommends

RUN echo "deb http://apt.postgresql.org/pub/repos/apt trusty-pgdg main" >> /etc/apt/sources.list
RUN wget --quiet --no-check-certificate -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-key add -
RUN apt-get -yq update
RUN apt-get -yq upgrade --no-install-recommends
RUN locale-gen --no-purge en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8
RUN apt-get -yq install postgresql-9.4 postgresql-contrib-9.4 postgresql-9.4-postgis-2.1 postgis
RUN echo "host    all             all             0.0.0.0/0               md5" >> /etc/postgresql/9.4/main/pg_hba.conf
RUN echo "listen_addresses = '*'" >> /etc/postgresql/9.4/main/postgresql.conf
RUN echo "port = 5432" >> /etc/postgresql/9.4/main/postgresql.conf

EXPOSE 5432

ADD start.sh /start.sh
RUN chmod 0755 /start.sh

CMD ["/start.sh"]

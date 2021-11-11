FROM postgres:9.4.8
MAINTAINER jann.kleen@gmail.com

RUN apt-get update && apt-get install -y postgresql-9.4-postgis

ADD 00_make_extensions.sh /docker-entrypoint-initdb.d/

FROM postgres:9.4

MAINTAINER Nicolas Delaby <ticosax@free.fr>

RUN apt-get update && apt-get upgrade -y &&\
    apt-get -qq install postgresql-$PG_MAJOR-postgis &&\
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

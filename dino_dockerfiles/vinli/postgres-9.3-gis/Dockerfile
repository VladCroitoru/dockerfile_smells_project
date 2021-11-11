FROM postgres:10.6
MAINTAINER Vinli Devs <dev@vin.li>

RUN apt-get update \
    && apt-get -y install postgresql-10-postgis-2.4 \
    && rm -rf /var/lib/apt/lists/*

# vim:set ft=dockerfile:
FROM postgres:11
ENV TERM xterm-256color

RUN apt-get update && \
    apt-get --fix-missing -y --force-yes --no-install-recommends install git ca-certificates && \
    git clone https://github.com/tada/pljava.git && \
    apt-get --fix-missing -y --force-yes --no-install-recommends install g++ maven && \
    apt-get --fix-missing -y --force-yes --no-install-recommends install postgresql-server-dev-11 libpq-dev && \
    apt-get --fix-missing -y --force-yes --no-install-recommends install libecpg-dev libkrb5-dev && \
    apt-get --fix-missing -y --force-yes --no-install-recommends install openjdk-8-jdk libssl-dev && \
    export PGXS=/usr/lib/postgresql/11/lib/pgxs/src/makefiles/pgxs.mk && \
    cd pljava && \
    git checkout tags/V1_5_2 && \
    mvn -Pwnosign clean install && \
    java -jar $(ls /pljava/pljava-packaging/target/pljava-pg11*-amd64-Linux-gpp.jar) && \
    cd ../ && \
    apt-get -y remove --purge --auto-remove git ca-certificates g++ maven postgresql-server-dev-11 libpq-dev libecpg-dev openjdk-8-jdk libkrb5-dev libssl-dev && \
    apt-get --fix-missing -y --force-yes --no-install-recommends install openjdk-8-jdk-headless && \
    apt-get -y clean autoclean autoremove && \
    rm -rf ~/.m2 /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD /docker-entrypoint-initdb.d /docker-entrypoint-initdb.d

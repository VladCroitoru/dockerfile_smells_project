# The file is used to build docker container for gitlab ci
FROM phusion/baseimage:focal-1.0.0

ENV LANG=en_US.UTF-8

RUN \
        apt-get update \
    && \
        apt-get install -y \
            iputils-ping \
            systemd \
            postgresql \
            postgresql-contrib \
            build-essential \
            cmake \
            libboost-all-dev \
            postgresql-server-dev-12 \
            git \
            libssl-dev \
            libreadline-dev \
            python3-pip \
    && \
        apt-get clean

RUN \
    python3 -mpip install \
        pexpect \
        psycopg2 \
        sqlalchemy

USER postgres
RUN  /etc/init.d/postgresql start \
    && psql --command "SELECT version();" \
    && psql --command "CREATE USER root WITH SUPERUSER CREATEDB;"

USER root
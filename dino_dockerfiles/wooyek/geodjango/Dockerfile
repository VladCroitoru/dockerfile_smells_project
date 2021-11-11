FROM ubuntu:18.04

MAINTAINER Janusz Skonieczny @wooyek
LABEL version="2.1.2"

# Pass the above envrioment variables through a file to the docker vm
# https://docs.docker.com/engine/reference/commandline/run/#set-environment-variables--e---env---env-file
# They will be used to create a default database on start
# Locale
# http://stackoverflow.com/a/27931669/260480

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    LC_TYPE=en_US.UTF-8 \
    PYTHONIOENCODING=utf-8 \
    DATABASE_NAME=application-db \
    DATABASE_PASSWORD=application-db-password \
    DATABASE_USER=application-user \
    DATABASE_HOST=127.0.0.1 \
    DATABASE_TEST_NAME=application-test-db \
    DATABASE_URL=postgis://application-user:application-db-password@127.0.0.1:5432/application-db \
    CPLUS_INCLUDE_PATH=/usr/include/gdal \
    C_INCLUDE_PATH=/usr/include/gdal \
    TZ=UTC

COPY docker-entrypoint.sh /usr/local/bin/

# Install tooling for test debuging and libraries needed by geodjango.

RUN chmod +x /usr/local/bin/docker-entrypoint.sh && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    apt-get update && apt-get -y upgrade && \
    apt-get install -y locales && \
    locale-gen en_US.UTF-8 && \
    apt-get install -y git git-flow unzip nano wget sudo curl build-essential && \
    apt-get install -y python python-dev python-pip python-virtualenv \
    python3 python3-dev python3-pip python3-venv python-enchant \
    python3.6 python3.6-dev python3.6-venv \
    spatialite-bin libsqlite3-mod-spatialite \
    postgresql-client-common libpq-dev \
    postgresql postgresql-contrib postgis \
    libproj-dev libfreexl-dev libgdal-dev gdal-bin && \
    python -m pip install pip -U && \
    python3 -m pip install pip -U && \
    pip2  install invoke tox coverage pylint gdal==2 pytest pytest-xdist pathlib -U && \
    pip3 install invoke tox coverage pylint gdal==2 pytest pytest-xdist -U && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["docker-entrypoint.sh"]

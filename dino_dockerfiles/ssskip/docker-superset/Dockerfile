FROM python:2.7
MAINTAINER ssskip

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python-dev \
    libsasl2-dev \
    libldap2-dev \
    && apt-get clean -y

RUN pip --no-cache-dir install superset==0.15.1 \
    mysqlclient \
    psycopg2==2.6.1 \
    pymssql \
    sqlalchemy-redshift 


ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PATH=$PATH:/home/superset/bin \
    PYTHONPATH=/home/superset/superset_config.py:$PYTHONPATH


WORKDIR /home/superset
COPY superset .
RUN groupadd -r superset && \
    useradd -r -m -g superset superset && \
    mkdir /home/superset/db && \
    chown -R superset:superset /home/superset && \
    chmod +x ./bin/*

USER superset



EXPOSE 8088
ENTRYPOINT ["superset"]
CMD ["runserver"]



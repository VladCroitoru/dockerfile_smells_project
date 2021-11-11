FROM ubuntu:latest

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libldap2-dev \
    libmysqlclient-dev \
    libsasl2-dev \
    libssl-dev \
    python3-dev \
    python3-pip \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install \
    impyla \
    mysqlclient \
    pandas==0.23.4 \
    psycopg2-binary \
    pybigquery \
    pyhive \
    pymssql \
    sqlalchemy==1.2.18 \
    superset

RUN fabmanager create-admin \
    --app superset \
    --username admin \
    --firstname admin \
    --lastname user \
    --email admin@fab.org \
    --password admin

RUN superset db upgrade && \
    superset load_examples &&\
    superset init

EXPOSE 8088

CMD ["superset", "runserver", "-d"]

FROM jupyter/datascience-notebook

USER root

RUN apt-get update -y && \
    apt-get install -y build-essential libreadline-dev zlib1g-dev flex bison libxml2-dev libxslt-dev libssl-dev wget

RUN mkdir -p /opt/scripts/dpkg && \
    cd /opt/scripts/dpkg && \
    wget --quiet https://s3-us-west-1.amazonaws.com/royseto-public/dpkg/postgres9.4.1-postgis2.1.5_9.4.1-2.1.5-local1_amd64.deb && \
    dpkg -i /opt/scripts/dpkg/postgres9.4.1-postgis2.1.5_9.4.1-2.1.5-local1_amd64.deb && \
    ldconfig

COPY newpath /tmp/newpath

RUN cat /tmp/newpath >> /etc/profile && \
    cat /tmp/newpath >> /home/jovyan/.bashrc && \
    rm -rf /tmp/newpath

USER jovyan

ENV PATH /usr/local/pgsql/bin:$PATH
ENV LD_LIBRARY_PATH /usr/local/pgsql/lib:$LD_LIBRARY_PATH
RUN /opt/conda/bin/pip2 install csvkit GeoAlchemy2 ipython-sql psycopg2 sqlalchemy
RUN /opt/conda/bin/pip3 install csvkit GeoAlchemy2 ipython-sql psycopg2 sqlalchemy


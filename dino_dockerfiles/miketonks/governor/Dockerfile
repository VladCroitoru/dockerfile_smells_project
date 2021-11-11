FROM postgres:9.4

RUN apt-get update && \
  apt-get install -y python-psycopg2 python-yaml python-dev libffi-dev libssl-dev python-pip

RUN pip install -U pip setuptools
RUN pip install python-etcd

RUN mkdir -p /governor/helpers
COPY governor.py /governor/governor.py
COPY helpers /governor/helpers
COPY postgres0.yml /governor/
COPY pg_hba.conf /governor/
COPY init.sql /governor/
COPY docker-entrypoint.sh /

RUN mkdir -p /data/postgres && \
  chown -R postgres /data && \
  chmod 700 /data/postgres && \
  chown postgres /governor && \
  chmod +x docker-entrypoint.sh

VOLUME  /data/postgres
WORKDIR /governor

ENTRYPOINT  ["/docker-entrypoint.sh"]

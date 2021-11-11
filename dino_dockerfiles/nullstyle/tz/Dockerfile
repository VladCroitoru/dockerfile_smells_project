FROM postgres:9.4

RUN apt-get update \
  &&  apt-get install -y postgis \
	&& rm -rf /var/lib/apt/lists/*
ADD data/tz.sql.gz /
ADD docker-entrypoint-initdb.d/* /docker-entrypoint-initdb.d/

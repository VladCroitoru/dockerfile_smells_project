from postgres:9.5

# Add testing repo for postgresql-hll
COPY testing.list /etc/apt/sources.list.d/

RUN \
	apt-get update                               &&\
	apt-get install -y postgresql-hll            &&\
	apt-get install -y postgresql-9.5-postgis    &&\
	apt-get install -y postgresql-9.5-pgrouting  &&\
	apt-get clean all                            &&\
	rm -rfv /var/lib/apt/lists/*

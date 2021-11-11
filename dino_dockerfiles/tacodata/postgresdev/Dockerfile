FROM tacodata/pythondev

MAINTAINER Greg Fausak <greg@tacodata.com>

# a simple postgres build
# postgres 9.4.0

RUN apt-get -y update &&\
	apt-get install -y wget ca-certificates libreadline-dev zlib1g-dev &&\
	apt-get -y upgrade

RUN groupadd -g 600 postgres &&\
	useradd postgres -m -g 600 -s /bin/bash -u 600 &&\
	/bin/echo 'set editing-mode vi' > /home/postgres/.inputrc

USER postgres
RUN mkdir /home/postgres/src
WORKDIR /home/postgres/src

RUN wget -q https://ftp.postgresql.org/pub/source/v9.4.0/postgresql-9.4.0.tar.gz &&\
	tar xzf postgresql-9.4.0.tar.gz

WORKDIR /home/postgres/src/postgresql-9.4.0

RUN ./configure && make -j 4

USER root
WORKDIR /home/postgres/src/postgresql-9.4.0

RUN make install

RUN mkdir -p /var/local/pgsql/data &&\
	mkdir -p /var/local/pgsql/logs &&\
	chown -R postgres:postgres /var/local/pgsql &&\
	echo 'PGDATA=/var/local/pgsql/data; export PGDATA' > /etc/profile.d/postgres_path.sh &&\
	echo 'PATH=/usr/local/pgsql/bin:$PATH' >> /etc/profile.d/postgres_path.sh

USER postgres
WORKDIR /home/postgres

# this creates a database called db which is the default database if none is mounted.
RUN /usr/local/pgsql/bin/initdb -D /var/local/pgsql/data
RUN /usr/local/pgsql/bin/pg_ctl -w -D /var/local/pgsql/data start &&\
	/usr/local/pgsql/bin/createdb db &&\
	/usr/local/pgsql/bin/pg_ctl -w -D /var/local/pgsql/data stop

USER root
WORKDIR /root

CMD [ '/bin/bash' ]

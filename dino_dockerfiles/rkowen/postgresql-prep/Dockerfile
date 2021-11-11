#
# A Docker container to prepare a PostgreSQL database (another container)
#

# change this to a recent image
FROM	ubuntu:14.04
MAINTAINER rk@owen.sj.ca.us

USER	root

RUN	apt-get -y -qq update
RUN	apt-get -y -qq upgrade

RUN	apt-get install -y -qq postgresql-client-9.3

ADD	docker.sql		/
ADD	oauth2-server.sql	/
ADD	testclient.sql		/

CMD	/usr/bin/psql						\
		--host=$POSTGRES_PORT_5432_TCP_ADDR		\
		--port=$POSTGRES_PORT_5432_TCP_PORT		\
	 	--username=postgres				\
		--file=/docker.sql

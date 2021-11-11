FROM ubuntu:16.04
MAINTAINER Rumesh <rehrumesh@hotmail.com>

RUN apt-get update
RUN apt-get install -y wget apt-transport-https cron zip
RUN wget -qO - https://www.mongodb.org/static/pgp/server-3.6.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.6.list
RUN apt-get update
RUN apt-get install -y mongodb-org=3.6.15 mongodb-org-server=3.6.15 mongodb-org-shell=3.6.15 mongodb-org-mongos=3.6.15 mongodb-org-tools=3.6.15 && \
	echo "mongodb-org hold" | dpkg --set-selections && \
	echo "mongodb-org-server hold" | dpkg --set-selections && \
	echo "mongodb-org-shell hold" | dpkg --set-selections && \
	echo "mongodb-org-mongos hold" | dpkg --set-selections && \
	echo "mongodb-org-tools hold" | dpkg --set-selections && \
	mkdir /backup

ENV CRON_TIME="0 0 * * *"

ADD run.sh /run.sh
VOLUME ["/backup"]
CMD ["/run.sh"]

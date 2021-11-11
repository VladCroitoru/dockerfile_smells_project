FROM debian:jessie

MAINTAINER Luis Ramos <momia191@gmail.com>

RUN apt-get update && apt-get install -y wget
RUN wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg |  apt-key add -
RUN echo "deb http://download.rethinkdb.com/apt jessie main" |  tee /etc/apt/sources.list.d/rethinkdb.list

RUN apt-get update \
	&& apt-get install -y rethinkdb python python-pip \
	&& apt-get install -y --no-install-recommends bind9-host    \
	&& rm -rf /var/lib/apt/lists/*
RUN mkdir /backup && chmod 777 /backup

VOLUME ["/backup"]
VOLUME ["/data"]

WORKDIR /data
RUN rethinkdb --version
CMD ["rethinkdb","--bind","all"]

EXPOSE 28015 29015 8080

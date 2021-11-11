FROM nodesource/vivid:LTS
MAINTAINER Prismatik Pty. Ltd. <david@prismatik.com.au>

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:ubuntu-lxc/lxd-stable
RUN apt-get update
RUN apt-get install -y golang
RUN apt-get install -y wget
RUN echo "deb http://download.rethinkdb.com/apt `lsb_release -cs` main" > /etc/apt/sources.list.d/rethinkdb.list
RUN wget -O- http://download.rethinkdb.com/apt/pubkey.gpg | apt-key add -
RUN apt-get update
RUN apt-get install -y rethinkdb python-pip
RUN rm -rf /var/lib/apt/lists/*
RUN pip install rethinkdb

RUN mkdir -p /go
ADD . /go/src/github.com/Prismatik/rethinkdb-backerupperer

ENV GOPATH=/go

WORKDIR /go/src/github.com/Prismatik/rethinkdb-backerupperer

RUN go get
RUN go install github.com/Prismatik/rethinkdb-backerupperer

EXPOSE 3000

CMD ["/go/bin/rethinkdb-backerupperer"]

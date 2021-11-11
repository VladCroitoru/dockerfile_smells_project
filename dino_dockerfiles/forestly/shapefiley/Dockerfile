FROM golang:wheezy

MAINTAINER Abhi Yerra <abhi@berkeley.edu>

RUN echo "deb http://http.debian.net/debian wheezy main" > /etc/apt/sources.list.d/pgdg.list
RUN echo "deb-src http://http.debian.net/debian wheezy main" > /etc/apt/sources.list.d/pgdg.list

RUN echo "deb http://http.debian.net/debian wheezy-updates main" > /etc/apt/sources.list.d/pgdg.list
RUN echo "deb-src http://http.debian.net/debian wheezy-updates main" > /etc/apt/sources.list.d/pgdg.list

RUN echo "deb http://security.debian.org/ wheezy/updates main" > /etc/apt/sources.list.d/pgdg.list
RUN echo "deb-src http://security.debian.org/ wheezy/updates main" > /etc/apt/sources.list.d/pgdg.list

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main" > /etc/apt/sources.list.d/pgdg.list

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y apt-utils wget ca-certificates
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get install -y --force-yes postgresql-9.3 postgis

ADD . /go/src/github.com/forestly/shapefiley

RUN cd /go/src/github.com/forestly/shapefiley && go get ./...
RUN go install github.com/forestly/shapefiley

RUN mkdir -p /tmp/shapefiley

WORKDIR /go/src/github.com/forestly/shapefiley

ENTRYPOINT /go/bin/shapefiley

EXPOSE 3002

FROM golang:latest
MAINTAINER Gian Carlo Val Ebao <gianebao@gmail.com>

RUN \
 apt-get update && apt-get -y upgrade &&\
 apt-get -y --no-install-recommends install locales &&\
 echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen &&\
 locale-gen en_US.UTF-8 &&\
 /usr/sbin/update-locale LANG=en_US.UTF-8

# Install Goose
RUN go get bitbucket.org/liamstask/goose/cmd/goose
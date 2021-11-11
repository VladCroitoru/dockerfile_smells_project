FROM debian:jessie
MAINTAINER Yuanl <yuanl.lee@gail.com>

RUN echo "deb http://apt.linode.com/ jessie main" > /etc/apt/sources.list.d/linode.list
COPY linode.gpg linode.gpg
RUN cat linode.gpg | apt-key add -
RUN apt-get update -y && apt-get install -y linode-cli cron

RUN adduser --system linodecli
USER linodecli
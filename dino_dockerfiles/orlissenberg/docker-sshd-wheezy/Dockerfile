FROM debian:wheezy

MAINTAINER Onno Lissenberg "https://github.com/orlissenberg"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN apt-get install -y python-software-properties python-pip git build-essential python python-dev

RUN echo 'root:root' |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN /etc/init.d/ssh restart

CMD    ["/usr/sbin/sshd", "-D"]

EXPOSE 22

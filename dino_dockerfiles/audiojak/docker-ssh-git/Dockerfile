FROM ubuntu:14.04

RUN apt-get -y update
RUN apt-get -y install openssh-server
RUN apt-get -y install git

# Setting openssh
RUN mkdir /var/run/sshd
RUN sed -i "s/#PasswordAuthentication yes/PasswordAuthentication no/" /etc/ssh/sshd_config

# Adding git user
RUN adduser --system git

# Updating shell to bash
RUN sed -i s#/home/git:/bin/false#/home/git:/bin/bash# /etc/passwd

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

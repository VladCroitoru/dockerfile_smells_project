#FROM rastasheep/ubuntu-sshd:14.04
FROM ubuntu:trusty
MAINTAINER Sreeprakash Neelakantan <sree@schogini.com>

RUN apt-get update && \
    apt-get install -y wget tree curl nano && \
    apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN passwd -d root

RUN sed -ri 's/^#IgnoreUserKnownHosts\s+.*/IgnoreUserKnownHosts yes/' /etc/ssh/sshd_config
RUN sed -ri 's/^PermitEmptyPasswords\s+.*/PermitEmptyPasswords yes/' /etc/ssh/sshd_config
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]

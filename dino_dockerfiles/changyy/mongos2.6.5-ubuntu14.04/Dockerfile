FROM ubuntu:14.04

# Install MongoDB
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y dist-upgrade
#RUN apt-get install -y mongodb-org
# Production Release (2.6.5) — 10/8/2014
RUN apt-get install -y mongodb-org=2.6.5 mongodb-org-server=2.6.5 mongodb-org-shell=2.6.5 mongodb-org-mongos=2.6.5 mongodb-org-tools=2.6.5

# MongoDB data
RUN mkdir -p /data/db

# Debug Tools
# ref: https://docs.docker.com/examples/running_ssh_service/
RUN apt-get -y install telnet openssh-server vim
RUN echo 'root:mongodb' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 27017
ENTRYPOINT ["usr/bin/mongos"]

FROM    ubuntu:13.10
MAINTAINER nicky.gurbani@gmail.com


RUN     apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
#RUN     echo "deb http://archive.ubuntu.com/ubuntu saucy universe" | tee -a /etc/apt/sources.list
RUN     echo "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen" | tee -a /etc/apt/sources.list.d/10gen.list

# Set locale
RUN     locale-gen --no-purge en_US.UTF-8
ENV     LC_ALL en_US.UTF-8
 

RUN     apt-get -y update
# Install dependencies
ENV     DEBIAN_FRONTEND noninteractive

RUN     apt-get install -y software-properties-common
RUN     apt-get -y install software-properties-common wget sudo net-tools

# Install  ssh server
RUN      apt-get install -y openssh-server
RUN      mkdir -p /var/run/sshd

RUN     add-apt-repository ppa:chris-lea/node.js
RUN     apt-get update
RUN     apt-get -y install nodejs python make g++ mongodb-10gen python-pip git
RUN     pip install supervisor
RUN     npm install databank-mongodb
RUN     mkdir /pumpio && git clone https://github.com/e14n/pump.io.git /pumpio/src
RUN     cd /pumpio/src && npm install
RUN     echo_supervisord_conf > /etc/supervisord.conf
ADD     Supervisorfile/ /pumpio/
ADD     pump.io.json/ /etc/
RUN     echo "[include]\nfiles = /pumpio/Supervisorfile\n" >> /etc/supervisord.conf
RUN     mkdir -p /data/db

EXPOSE  22 80
CMD ["/usr/local/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"] 

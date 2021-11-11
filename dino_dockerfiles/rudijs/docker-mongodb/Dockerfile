############################################################
# Dockerfile to build MongoDB container images
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu 12.04 LTS
FROM    ubuntu:12.04

# File Author / Maintainer
MAINTAINER rudijs <ooly.me@gmail.com>

# Update the repository sources list, update and upgrade
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list

RUN apt-get update

RUN apt-get upgrade -y

################## BEGIN INSTALLATION ######################
# Install MongoDB Following the Instructions at MongoDB Docs
# Ref: http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/

# Add the package verification key
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

# Add MongoDB to the repository sources list
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/10gen.list

# Add to the repository sources list
# MongoDB database
# pwgen for user account creation
# openssh-server for network connect
# tmux advanced terminal
# supervisor to start network services
# sudo for user account admin services

RUN apt-get update

RUN apt-get install -y mongodb-10gen pwgen openssh-server tmux supervisor sudo

# Configure sudo
RUN echo '%sudo   ALL=NOPASSWD: ALL' >> /etc/sudoers

# Configure sshd and start up
RUN mkdir /var/run/sshd
RUN sed -i.bak s/PermitRootLogin\ yes/PermitRootLogin\ no/ /etc/ssh/sshd_config
ADD ./supervisord_sshd.conf /etc/supervisor/conf.d/sshd.conf

# Backup original MongoDB config
RUN mv /etc/mongodb.conf /etc/mongodb.orig.conf

# Copy in custom MongoDB config
ADD ./mongodb.conf /etc/mongodb.conf

# Configure mongod start up
ADD ./supervisord_mongodb.conf /etc/supervisor/conf.d/mongodb.conf

# Install jq: http://stedolan.github.io/jq/
RUN wget -nv http://stedolan.github.io/jq/download/linux64/jq -O /usr/bin/jq
RUN chmod 755 /usr/bin/jq

# Script to add user and copy supervisord configs
ADD ./start.sh /start.sh

# Set as executable
RUN chmod 755 /start.sh

ENTRYPOINT ["/bin/sh", "-c", "/start.sh"]

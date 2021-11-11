FROM phusion/baseimage:0.9.15
MAINTAINER Sean Chatman <xpointsh@gmail.com>

# Cleaning lists to make sure we have the most recent.
# There were problems with trusting the parent lists.
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /var/lib/apt/lists/partial/*
RUN apt-get clean
RUN apt-get update
RUN apt-get -y upgrade

RUN apt-get install -y curl openjdk-7-jdk unzip wget

RUN echo "deb http://pkg.jenkins-ci.org/debian binary/" > /etc/apt/sources.list.d/jenkins.list
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y jenkins

VOLUME /var/lib/jenkins
VOLUME /var/lib/docker

###### Installing Docker in Docker ######

# Install basics.
RUN apt-get update -qq
RUN apt-get install -qqy iptables ca-certificates lxc

# Install Docker from Docker Inc. repositories.
RUN apt-get install -qqy apt-transport-https
RUN echo deb https://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
RUN apt-get update -qq
RUN apt-get install -qqy lxc-docker

# Install the magic wrapper.
ADD ./wrapdocker /etc/my_init.d/wrapdocker
RUN chmod +x /etc/my_init.d/wrapdocker
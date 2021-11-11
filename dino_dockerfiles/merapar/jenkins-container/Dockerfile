# vim: ft=dockerfile
###############################################################################
# Jenkins with DooD (Docker outside of Docker)
# http://github.com/merapar/docker-jenkins
# Author: Dennis Bell <dennis.bell@merapar.com>
# Based on:
# * http://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci
###############################################################################

FROM jenkins/jenkins:2.176.2
MAINTAINER Dennis Bell <dennis.bell@merapar.com>
ENV JENKINS_UC="https://updates.jenkins.io"

# Install necessary packages
USER root
RUN apt-get update \
      && apt-get install -y sudo python-pip \
      && rm -rf /var/lib/apt/lists/*

# Install docker-engine
# We will bind the socket to use the host docker engine from the container

ARG docker_version=19.03.1

RUN curl -sSL https://get.docker.com/ | sh

# Make sure jenkins user has docker privileges to use the socket
RUN usermod -aG docker jenkins

# Make sure jenkins scripts can run sudo
RUN echo 'jenkins ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# Install initial plugins
USER jenkins

# Get these using the following trick: 
#  https://stackoverflow.com/questions/9815273/how-to-get-a-list-of-installed-jenkins-plugins-with-name-and-version-pair
COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt


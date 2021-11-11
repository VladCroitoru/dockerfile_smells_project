FROM jenkins:latest
MAINTAINER Jérémy SEBAN <jeremy@seban.eu>

USER root

RUN echo "deb http://apt.dockerproject.org/repo debian-jessie main" > /etc/apt/sources.list.d/docker.list
RUN apt-get update
RUN apt-get install -y --force-yes docker-engine sudo
RUN echo "jenkins ALL = (ALL) NOPASSWD: /usr/bin/docker" > /etc/sudoers.d/docker
RUN usermod -aG docker jenkins

USER jenkins

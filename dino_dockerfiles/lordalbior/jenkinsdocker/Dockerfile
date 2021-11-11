FROM jenkins:latest
MAINTAINER Albert Almeida

ENV DEBIAN_FRONTEND=noninteractive

USER root

RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y libc6:i386 lib32stdc++6 lib32z1 lib32z1-dev 
RUN apt-get install -y sudo 
RUN usermod -aG sudo jenkins
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers


WORKDIR /var/jenkins_home

USER jenkins


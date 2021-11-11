FROM maven:3.3.3-jdk-8 

MAINTAINER Efthymios Sarmpanis

RUN apt-get update
RUN apt-get install -y apt-transport-https ca-certificates
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list
RUN apt-get update
RUN apt-get purge lxc-docker
RUN apt-get install -y docker-engine
RUN usermod -aG docker $USER
RUN service docker start
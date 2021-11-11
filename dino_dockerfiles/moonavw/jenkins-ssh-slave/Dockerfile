FROM jenkinsci/ssh-slave:latest
MAINTAINER Tao Wang <moonavw@gmail.com>

RUN apt-get -qq update \
   && apt-get -qq -y install \
   curl

RUN curl -sSL https://get.docker.com/ | sh

RUN usermod -a -G staff,docker jenkins

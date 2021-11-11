
FROM centos:7

MAINTAINER Sven Malvik <sven@malvik.de>

COPY docker-main.repo /etc/yum.repos.d/

RUN yum update -y && yum install -y epel-release 
RUN yum install -y \
  emacs \
  python-pip \
  jq \
  httpie \
  docker-engine-1.11.2 \
  ansible \
  git

RUN pip install --upgrade pip
RUN pip install docker-compose 

RUN mkdir /etc/emacs
COPY init.el /etc/emacs/
COPY dockerfile-mode.el /etc/emacs/

WORKDIR /home

CMD emacs -q -l /etc/emacs/init.el

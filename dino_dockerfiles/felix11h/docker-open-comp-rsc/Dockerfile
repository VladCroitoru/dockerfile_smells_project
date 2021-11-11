FROM ubuntu:16.04
MAINTAINER felix11h.dev@gmail.com

USER root

RUN apt-get -qy update
RUN apt-get install -qy apt-utils python python-dev python-pip git screen 

RUN pip install --upgrade pip
RUN pip install numpy scipy matplotlib sumatra gitpython configparser 

RUN useradd -ms /bin/bash docker
USER docker

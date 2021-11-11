FROM ubuntu:trusty
MAINTAINER maglovato

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y --force-yes software-properties-common
RUN apt-get install -y --force-yes python-software-properties
RUN add-apt-repository -y ppa:fkrull/deadsnakes
RUN apt-get update -y
RUN apt-get install -y --force-yes python2.6 python2.6-dev
RUN apt-get install -y telnet
RUN apt-get install -y curl
RUN apt-get install -y openssh-client
RUN apt-get install -y unzip

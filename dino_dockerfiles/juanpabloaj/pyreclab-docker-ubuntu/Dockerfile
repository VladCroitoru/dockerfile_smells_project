FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y g++ cmake libboost-dev
RUN apt-get install -y python-dev
RUN apt-get install -y vim git curl

WORKDIR /root

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py

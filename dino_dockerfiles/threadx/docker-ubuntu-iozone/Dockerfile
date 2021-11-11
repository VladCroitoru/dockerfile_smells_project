FROM       ubuntu:14.04

MAINTAINER Howard Young "https://github.com/threadx"

RUN apt-get update --fix-missing

RUN apt-get -y install wget make gcc

RUN wget http://www.iozone.org/src/current/iozone3_430.tar
RUN tar xvf iozone3_430.tar 
RUN cd iozone3_430/src/current; make linux; cp iozone /usr/bin
 
cmd     /bin/bash

FROM ubuntu:trusty

MAINTAINER Steven Edouard <steven.edouard1@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y
RUN apt-get -qq update -y
RUN apt-get install -y nodejs npm -y

#RUN sudo apt-get install software-properties-common -y
#RUN sudo add-apt-repository ppa:djcj/vlc-stable -y
#RUN sudo apt-get update -y
#RUN sudo apt-get upgrade -y
#RUN sudo apt-get install ffmpeg -y

VOLUME ["/data"]

ADD . /data


FROM ghdl/runner:latest

MAINTAINER Mario Barbareschi <mario.barbareschi@unina.it>

RUN apt-get update && \ 
    apt-get -y upgrade && \
    apt-get -y install cmake make git gtkwave

ADD ./ /opt

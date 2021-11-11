FROM ubuntu
MAINTAINER Luca Marcelli

RUN apt-get update
RUN apt-get install -y git build-essential nasm python3 python mono-complete gdb curl wget unzip vim nano default-jdk

RUN cd /opt; git clone https://github.com/radare/radare2.git; cd radare2; ./sys/install.sh

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

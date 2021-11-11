FROM ubuntu:xenial

#COPY forkethereum.tar.gz /forkethereum.tar.gz
#RUN tar -xvf /forkethereum.tar.gz

COPY . /forkethereum
WORKDIR /forkethereum
RUN apt-get update -qq && apt-get install -yqq sudo
RUN apt-get install -yqq vim
RUN ./install.sh

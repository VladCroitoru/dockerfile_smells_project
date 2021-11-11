FROM ubuntu:14.04

MAINTAINER Jonathan Robin Langford <jrobinlangford@gmail.com>

RUN apt-get update && \
	apt-get -y install curl git python make g++

RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -

RUN apt-get install -y nodejs

RUN npm install -g strongloop

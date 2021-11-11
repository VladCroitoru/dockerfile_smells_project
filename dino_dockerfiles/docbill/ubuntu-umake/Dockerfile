FROM ubuntu
MAINTAINER Bill C Riemers https://github.com/docbill

RUN apt-get update -y && \
	apt-get install -y software-properties-common python-software-properties sudo && \
	add-apt-repository ppa:ubuntu-desktop/ubuntu-make && \
	apt-get update -y && \
	apt-get install -y ubuntu-make && \
	apt-get clean -y all


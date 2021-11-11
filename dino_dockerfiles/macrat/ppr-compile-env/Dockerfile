FROM ubuntu:latest

MAINTAINER MacRat <m@crat.jp>

RUN apt-get update \
	&& apt-get install -y software-properties-common \
	&& add-apt-repository ppa:team-gcc-arm-embedded/ppa \
	&& apt-get update \
	&& apt-get install -y gcc-arm-none-eabi git doxygen make python3 python3-pip \
	&& pip3 install pep8 pyflakes

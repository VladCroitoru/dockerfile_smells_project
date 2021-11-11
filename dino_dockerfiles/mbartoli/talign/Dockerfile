FROM ubuntu:14.04
MAINTAINER Mike Bartoli "michael.bartoli@pomona.edu"

RUN apt-get update && apt-get install -y build-essential \
	python \
	python-dev \
	python-setuptools \
#	python-numpy \
	python-imaging \
	git \
	curl \
	libffi-dev \
	libssl-dev

RUN curl https://bootstrap.pypa.io/get-pip.py | python

RUN pip install requests[security]

RUN pip install numpy

RUN pip install PIL --allow-external PIL --allow-unverified PIL 

WORKDIR /home
RUN git clone https://github.com/mbartoli/tAlign

WORKDIR /home/tAlign



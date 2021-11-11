# Base Image
FROM ubuntu:16.04

# Metadata
LABEL base.image="Ubuntu 16.04"
LABEL version="SMC-Heterogeneity Release 5"
LABEL software="PhyloWGS"
LABEL software.version="smchet5"
LABEL description="Application for inferring subclonal composition and evolution from whole-genome sequencing data"
LABEL website="https://github.com/morrislab/phylowgs"
LABEL documentation="https://github.com/morrislab/phylowgs"
LABEL license="https://github.com/morrislab/phylowgs"
LABEL tags="Genomics"

# Maintainer
MAINTAINER Tiandao Li <litd99@gmail.com>

# Installation
#RUN apt-get install -y --no-install-recommends libnss-sss
RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
	git \
	gsl-bin \
	libgsl0-dev \
	libnss-sss \
	python-lxml \
	python-numpy \
	python-pip \
	python-qt4 \
	python-scipy \
	python-setuptools \
	python-six

RUN easy_install -U ete2
RUN git clone https://github.com/morrislab/phylowgs.git
RUN cd phylowgs/ && g++ -o mh.o -O3 mh.cpp  util.cpp `gsl-config --cflags --libs`


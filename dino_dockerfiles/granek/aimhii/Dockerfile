# AIMHII
#
# VERSION               0.0.1

FROM debian:jessie
MAINTAINER Josh Granek <joshua.granek@duke.edu>

LABEL Description="This image is used to set up a container for running AIM-HII"


RUN apt-get update && apt-get install -y --no-install-recommends \
	make \
	git \
	bwa \
	samtools \
	python-pip \
	python-numpy \
	zlib1g-dev \
	sra-toolkit \
	python-matplotlib \
	libgsl0-dev \
	wget \
	curl \
	gcc \
	g++ \
	python-dev
#	python-biopython \
#	cython \
#	python-pysam \

# RUN apt-get install -y curl python-pysam

# RUN pip install numpy
RUN pip install pysam
RUN pip install aimhii

WORKDIR /root/

RUN	cd ~ && \
	wget "https://drive.google.com/uc?export=download&id=0B7KhouP0YeRAc2xackxzRnFrUEU" -O ea-utils.1.1.2-806.tar.gz && \
	tar -xvf ea-utils.1.1.2-806.tar.gz && \
	cd ea-utils.1.1.2-806 && \
	make && \
	cp -a fastq-mcf /usr/local/bin/ && \
	cp -a fastq-join /usr/local/bin/ && \
	cd ~ && \
	rm -rf ea-utils.1.1.2-806 ea-utils.1.1.2-806.tar.gz

RUN 	git clone https://github.com/granek/aimhii.git

WORKDIR /root/aimhii/example_analysis

ENV PATH $PATH:/usr/lib/samtools

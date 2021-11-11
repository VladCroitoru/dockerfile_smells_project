##################################################
# docker container for ENCODE ATAC-seq pipeline
##################################################

FROM continuumio/miniconda3
# this is based on debian 8.5

# File Author / Maintainer 
MAINTAINER Claus J. Scholz <cscholz@uni-bonn.de>

# start the installation
# RUN apt-get upgrade -y

RUN apt-get remove --yes openjdk-7-jre-headless
RUN apt-get update && apt-get install -y wget \
	git \
	libxp6 \
	libxt6 \
	ghostscript

RUN echo "deb ftp://ftp.nl.debian.org/debian jessie-backports main contrib non-free" >> /etc/apt/sources.list.d/backports.list
RUN apt-get -y update && apt-get install -y -t jessie-backports openjdk-8-jre-headless ca-certificates-java

USER root

WORKDIR /root/

RUN wget https://github.com/leepc12/BigDataScript/blob/master/distro/bds_Linux.tgz?raw=true -O bds_Linux.tgz
RUN tar zxvf bds_Linux.tgz
RUN echo 'export PATH=$PATH:$HOME/.bds' >> /root/.bashrc 
RUN echo 'export _JAVA_OPTIONS="-Xms256M -Xmx728M -XX:ParallelGCThreads=1"' >> /root/.bashrc

RUN git clone https://github.com/kundajelab/atac_dnase_pipelines /root/atac_dnase_pipelines --recursive
WORKDIR /root/atac_dnase_pipelines

RUN apt-get update && apt-get install -y build-essential

RUN /root/atac_dnase_pipelines/install_dependencies.sh

# RUN /root/atac_dnase_pipelines/install_genome_data.sh mm10 /root/genomes
# RUN /root/atac_dnase_pipelines/install_genome_data.sh hg38 /root/genomes

RUN apt-get clean
RUN apt-get remove --yes --purge build-essential

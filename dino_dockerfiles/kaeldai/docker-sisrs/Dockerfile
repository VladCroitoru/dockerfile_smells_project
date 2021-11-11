FROM debian:jessie
MAINTAINER Kael Dai, kdai1@asu.edu

RUN apt-get update -y

RUN apt-get install -y \
    git \
    bowtie2 \
    velvet \
    samtools \
    parallel

RUN git clone -b dockerized https://github.com/kaeldai/SISRS.git



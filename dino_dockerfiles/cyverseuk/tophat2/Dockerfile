FROM ubuntu:16.04

LABEL ubuntu.version="16.04" bowtie2.version="2.2.6" samtools.version="0.1.18" tophat.version="2.1.0" maintainer="Alice Minotto, @ Earlham Institute"

USER root

RUN apt-get -y update && apt-get -yy install tophat

WORKDIR /data/

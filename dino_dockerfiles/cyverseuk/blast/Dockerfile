FROM ubuntu:16.04

LABEL ubuntu.version="16.04" blast.version="2.2.31" maintainer="Alice Minotto, @ Earlham Institute" 

USER root

RUN apt-get -y update && apt-get -yy install ncbi-blast+

WORKDIR /data/


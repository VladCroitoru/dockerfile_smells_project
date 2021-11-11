FROM ubuntu:16.04

LABEL ubuntu.version="16.04" trimmomatic.version="0.36" maintainer="Alice Minotto, @ Earlham Institute"

USER root

RUN apt-get -y update && apt-get -yy install default-jre \
    wget \
    unzip && \
    wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip && \
    unzip Trimmomatic-0.36.zip && \
    rm Trimmomatic-0.36.zip && \
    mv Trimmomatic-0.36 /data/ 

WORKDIR /data/

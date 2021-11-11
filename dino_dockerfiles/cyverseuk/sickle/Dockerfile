FROM ubuntu:16.04

#fill in the next line with all <package>.version you will install
LABEL ubuntu.version="16.04" sickle.version="1.33" maintainer="Alice Minotto, @ Earlham Institute" 

USER root

RUN apt-get -y update && apt-get -yy install gcc \
    libz-dev \
    make \
    wget && \
    wget https://github.com/najoshi/sickle/archive/v1.33.tar.gz && \
    tar -zxvf v1.33.tar.gz && \
    rm v1.33.tar.gz && \
    cd sickle-1.33 && \
    make && \
    mv sickle /bin/

WORKDIR /data/

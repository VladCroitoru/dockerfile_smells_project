# Docker image based on Ubuntu
FROM ubuntu:latest
MAINTAINER Nate Matteson <natem@scripps.edu>

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-setuptools \
    python3-docutils \
    python3-flask \
    default-jre \
    git \
    python3-pip \
    bwa \
    tabix \
    bcftools

# Install samtools and the like.
RUN apt update && \
    apt install --yes wget libcurl3-gnutls && \
    wget http://mirrors.kernel.org/ubuntu/pool/universe/s/samtools/samtools_1.4.1-1build1_amd64.deb && \
    wget http://mirrors.kernel.org/ubuntu/pool/universe/h/htslib/libhts2_1.5-1_amd64.deb && \
    dpkg -i samtools_*.deb libhts2_*.deb && \
    rm *.deb && \
    apt clean

ENV JAVA_HOME  /usr/lib/jvm/java-8-openjdk-amd64

# Clone the iVar repository.
WORKDIR /home/user
RUN mkdir /wd
RUN git clone https://github.com/watronfire/iVar.git
WORKDIR /home/user/iVar

# Install python requirements.
RUN pip3 install -r requirements.txt
RUN pip3 install snakemake

# Initiate docker with the command:
# docker run -it --name:iVar -v <pathToWD>:/home/user/wd watronfire/ivar
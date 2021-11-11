FROM ubuntu:14.04

WORKDIR /opt

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python && \
    apt-get install -y python3-pip && \
    apt-get install -y wget \
    curl \
    unzip \
    gcc \
    python-dev \
    python-setuptools \
    git \
    less \
    lynx \
    hdfview \
    aufs-tools \
    automake \
    bedtools \
    btrfs-tools \
    build-essential \
    dpkg-sig \
    iptables \
    samtools \
    software-properties-common

# Installing Java 8.... dockerfile snippet from https://github.com/dockerfile/java/blob/master/oracle-java8/Dockerfile
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV JAVA_LIBRARY_PATH /usr/lib/jni

# Added from GATK4 public (Getting R setup)
RUN mkdir -p /usr/local/lib/R/ && \
    mkdir -p ~/site-library && \
    ln -sFv ~/site-library /usr/local/lib/R/site-library
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
    add-apt-repository "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" && \
    apt-get update && \
    apt-get install -y --force-yes \
        r-base-dev=3.1.3-1trusty \
        r-base-core=3.1.3-1trusty

WORKDIR /opt

RUN git clone --recursive https://github.com/cgrlab/gatk-protected.git
RUN tar -xjvf /opt/gatk-protected/GenomeAnalysisTK-3.6.tar.bz2 
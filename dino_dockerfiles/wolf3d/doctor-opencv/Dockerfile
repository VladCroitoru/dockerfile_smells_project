# Pull base image
FROM debian:jessie


RUN echo "deb http://ftp.pl.debian.org/debian jessie main" > /etc/apt/sources.list

# Update packages
RUN apt-get clean -y && \
    apt-get autoclean -y && \
    apt-get autoremove -y 

RUN apt-get update && apt-get install -y \
    build-essential cmake pkg-config \
    libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev \
    libgtk2.0-dev openexr libopenexr6 libopenexr-dev \
    libatlas-base-dev gfortran \
    libtbb2 libtbb-dev zlib1g-dbg zlib1g zlib1g-dev \
    python2.7-dev python3-dev wget curl unzip bzip2 && \
    wget https://bootstrap.pypa.io/get-pip.py && python2.7 get-pip.py && \
    pip install numpy

RUN apt-get clean -y && \
    apt-get autoclean -y && \
    apt-get autoremove -y

ADD build-script /build-script

RUN /bin/sh /build-script

#vim:ts=4

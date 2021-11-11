# sterling312/base
#
FROM ubuntu:14.04

MAINTAINER Gang Huang doc.n.try@gmail.com

# compiled package install
RUN apt-get update
RUN apt-get install -y git-core wget curl vim build-essential \
    libgeos-dev gfortran liblapack-dev liblas-dev gdal-bin \
    g++ postgresql python-dev libfreetype6-dev unzip 

# install s3cmd for python2.7
RUN apt-get install -y python-pip
RUN pip install s3cmd==1.0.1

# need to move requirements.txt over
ADD requirements.txt /root/requirements.txt
RUN apt-get install -y python-numpy python-scipy python-matplotlib python-lxml python-gdal
#RUN apt-get install -y python3-numpy python3-scipy python3-matplotlib python3-lxml python3-gdal
#RUN pip install numpy scipy matplotlib lxml gdal
RUN pip install -r /root/requirements.txt

# install redis-servier
RUN cd /; wget http://download.redis.io/releases/redis-3.0.5.tar.gz
RUN tar xzf /redis-3.0.5.tar.gz
RUN cd /redis-3.0.5; make
ENV REDISPATH /redis-3.0.5/src

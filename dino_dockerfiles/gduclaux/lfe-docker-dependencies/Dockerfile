# Pull base image.
FROM ubuntu:trusty

MAINTAINER Guillaume Duclaux

RUN apt-get update -y

RUN apt-get install -y git python-pip python-dev 

RUN pip install -U setuptools
RUN pip install -U pip  # fixes AssertionError in Ubuntu pip
RUN pip install jupyter matplotlib
RUN apt-get install -y python-mpltoolkits.basemap python-skimage
RUN pip install scipy
RUN pip install numpy
RUN pip install cmocean

RUN apt-get install wget
RUN wget http://download.osgeo.org/gdal/2.1.3/gdal-2.1.3.tar.gz -O /tmp/gdal-2.1.3.tar.gz && \
tar -x -f /tmp/gdal-2.1.3.tar.gz -C /tmp 

RUN cd /tmp/gdal-2.1.3 && \
  ./configure \
    --prefix=/usr \
    --with-python \
    --with-geos \
    --with-geotiff \
    --with-jpeg \
    --with-png \
    --with-expat \
    --with-libkml \
    --with-openjpeg \
    --with-pg \
    --with-curl \
    --with-spatialite && \
  make && make install 

RUN pip install GDAL==2.1.3


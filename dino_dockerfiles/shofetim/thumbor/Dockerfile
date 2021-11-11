FROM ubuntu:15.04

MAINTAINER Jordan Schatz "jordan@noionlabs.com"

RUN apt-get update

RUN apt-get install -y python-pip build-essential python-dev curl \
    python-pycurl python-numpy python-opencv webp libpng-dev libtiff-dev \
    libjasper-dev libjpeg-dev libdc1394-22-dev libdc1394-22 libdc1394-utils

# "Extras"
RUN apt-get install -y libjpeg-turbo-progs

RUN pip install thumbor

VOLUME /data

EXPOSE 8888

CMD ["thumbor"]

FROM ubuntu:15.04

MAINTAINER Moshen Chan <moshen@gmail.com>

# Install python
RUN apt-get update
RUN apt-get install -y python-dev python-software-properties python-pip libzmq-dev libjpeg-dev zlib1g-dev

# symlink the native extensions so Python can pick them up and build PIL with zlib support
RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libboost_python.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libboost_thread.so /usr/lib

# Install TileStache
RUN pip install http://github.com/TileStache/TileStache/tarball/master

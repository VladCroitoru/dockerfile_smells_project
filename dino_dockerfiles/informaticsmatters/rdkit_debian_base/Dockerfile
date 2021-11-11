# base image for RDKit builds
FROM debian:buster
MAINTAINER Tim Dudgeon <tdudgeon@informaticsmatters.com>

RUN apt-get update && apt-get install -y \
 build-essential\
 python-numpy\
 cmake\
 python-dev\
 python-pip\
 sqlite3\
 libsqlite3-dev\
 libboost-dev\
 libboost-system-dev\
 libboost-thread-dev\
 libboost-serialization-dev\
 libboost-python-dev\
 libboost-regex-dev\
 swig\
 git\
 wget\
 zip &&\
 apt-get upgrade -y &&\
 apt-get clean -y
 
# add the rdkit user, but don't switch to it yet 
RUN useradd -m rdkit 

FROM ubuntu:14.04
MAINTAINER Haoyang Zeng  <haoyangz@mit.edu>

RUN sudo apt-get update
RUN sudo apt-get -q -y install r-base openssh-client python-pip
RUN sudo apt-get -q -y install python-dev

RUN pip install numpy
RUN pip install python-Levenshtein
RUN sudo apt-get -q -y install libhdf5-dev
RUN pip install h5py

RUN mkdir /scripts/
ADD helper.py /scripts/
ADD cluster.py /scripts/
ADD cutoff_pvalue.py /scripts/

WORKDIR /scripts/

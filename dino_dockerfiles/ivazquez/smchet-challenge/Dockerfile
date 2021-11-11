############################################################
# Dockerfile to build cloneHD workflow container
# Based on Ubuntu
############################################################

FROM ubuntu

# File Author / Maintainer
MAINTAINER Ignacio Vazquez-Garcia <ivg@sanger.ac.uk>

# Install software
RUN apt-get update && apt-get install -y make gfortran gcc \
build-essential libgsl2 gsl-bin libgsl-dev libboost-all-dev \
libblas-dev liblapack-dev git perl python-pip gzip

WORKDIR /opt

# Install python modules
RUN pip install PyVCF

# Install cloneHD
RUN git clone https://github.com/ivazquez/cloneHD.git && cd cloneHD && git checkout smchet
RUN cd cloneHD/src && mkdir ../build && make -f Makefile.farm

# Copy scripts to `WORKDIR`
COPY smchet_workflow.sh *.pl *.py *.cpp Makefile ./
RUN make -f ./Makefile
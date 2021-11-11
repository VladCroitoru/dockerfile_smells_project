FROM ubuntu:16.04
MAINTAINER Kelly Rowland <kellylynnerowland@gmail.com>

RUN apt-get update &&\
    apt-get install -y --no-install-recommends apt-utils &&\
    apt-get install -y build-essential &&\
    apt-get install -y wget &&\
    apt-get install -y swig &&\
    apt-get install -y libopenmpi-dev &&\
    apt-get install -y cmake

# build HDF5
RUN wget https://support.hdfgroup.org/ftp/HDF5/prev-releases/hdf5-1.10/hdf5-1.10.1/src/hdf5-1.10.1.tar.gz 
RUN tar zxf hdf5-1.10.1.tar.gz &&\
    mv hdf5-1.10.1 hdf5-setup &&\
    cd hdf5-setup; ./configure --prefix=/usr/local &&\
    make && make install

# cleanup
RUN cd /; rm -rf hdf5*
RUN apt-get -yq autoremove
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# test
RUN mpicc --version

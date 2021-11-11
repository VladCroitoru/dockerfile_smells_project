# Dockerfile for Python based RDKit implementation
# Based on Debian.
# Includes InCHI support.
# WARNING: this takes about an hour to build

FROM informaticsmatters/rdkit_debian_base
MAINTAINER Tim Dudgeon <tdudgeon@informaticsmatters.com>

RUN apt-get update &&\
 apt-get upgrade -y &&\
 apt-get clean -y
 
ENV RDKIT_BRANCH=master
RUN git clone -b $RDKIT_BRANCH --single-branch https://github.com/rdkit/rdkit.git

ENV RDBASE=/rdkit
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$RDBASE/lib:/usr/lib/x86_64-linux-gnu
ENV PYTHONPATH=$PYTHONPATH:$RDBASE

RUN mkdir $RDBASE/build
WORKDIR $RDBASE/build

RUN nproc=$(getconf _NPROCESSORS_ONLN) &&\
 cmake -DRDK_BUILD_INCHI_SUPPORT=ON -DRDK_BUILD_PYTHON_WRAPPERS=ON .. &&\
 make -j $(( nproc > 2 ? nproc - 2 : 1 )) &&\
 make install
# clean task has been removed as it was removing files that had been 'install'ed

#USER rdkit
WORKDIR $RDBASE

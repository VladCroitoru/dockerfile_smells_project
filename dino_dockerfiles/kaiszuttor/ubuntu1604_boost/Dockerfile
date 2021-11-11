FROM espressomd/buildenv-espresso-ubuntu:python
MAINTAINER Kai Szuttor <kai@icp.uni-stuttgart.de>

USER root

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
        perl \
        module-init-tools \
        libbz2-ocaml-dev

#RUN cd /usr/bin  && rm gcc g++ && ln -s gcc-4.9 gcc && ln -s g++-4.9 g++

RUN apt-get purge -y libboost* && \
    git clone --recursive --branch boost-1.61.0 https://github.com/boostorg/boost.git && \
    cd boost && \
    ./bootstrap.sh --prefix=/usr/local && \
    echo "using mpi ;" >> project-config.jam && \
    ./b2 headers && \
    ./b2 install --prefix=/usr/local

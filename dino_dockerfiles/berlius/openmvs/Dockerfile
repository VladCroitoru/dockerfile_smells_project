FROM ubuntu:16.04

MAINTAINER berlius <berlius52@yahoo.com>


# Dependencies 

RUN apt-get update && apt-get install -y \
    git \
    mercurial \
    cmake \
    libpng-dev \
    libjpeg-dev \
    libtiff-dev \
    libglu1-mesa-dev \
    libboost-iostreams-dev \
    libboost-program-options-dev \
    libboost-system-dev \
    libboost-serialization-dev \
    libopencv-dev \
    libcgal-dev \
    libcgal-qt5-dev \
    libatlas-base-dev \
    libsuitesparse-dev 

# Eigen
RUN mkdir eigen && cd eigen
WORKDIR "/root/eigen"
RUN hg clone https://bitbucket.org/eigen/eigen#3.2 /root/eigen/eigen
RUN mkdir eigen_build 
RUN cd eigen_build
RUN cmake . /root/eigen/eigen
RUN make && make install && cd .. && cd ..

# Ceres
RUN mkdir ceres && cd ceres
WORKDIR "/root/ceres"
RUN git clone https://ceres-solver.googlesource.com/ceres-solver /root/ceres/ceres-solver
RUN mkdir ceres_Build && cd ceres_Build
RUN cmake . /root/ceres/ceres-solver -DMINIGLOG=ON -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF
RUN make && make install && cd .. && cd ..


# VCGLib 

RUN git clone https://github.com/cdcseacave/VCG.git /root/vcglib


# OpenMVS 
RUN mkdir openMVS && cd openMVS
WORKDIR "/root/openMVS"
RUN git clone https://github.com/cdcseacave/openMVS.git /root/openMVS/openMVS
RUN mkdir openMVS_Build && cd openMVS_Build 
RUN cmake . /root/openMVS/openMVS -DCMAKE_BUILD_TYPE=RELEASE -DVCG_DIR="/root/vcglib" 
RUN make && make install

ENV PATH=/usr/local/bin/OpenMVS:$PATH

WORKDIR "/root"
CMD ["/bin/bash"]


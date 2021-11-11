FROM ubuntu:16.04
MAINTAINER Masahiro Wada <argon.argon.argon@gmail.com>

ADD bashrc /root/

#System Update & Install packages
RUN apt-get update
RUN apt-get -y -q upgrade
RUN apt-get -y install git wget cmake vim build-essential

#Anaconda3
WORKDIR /tmp
ENV ANACONDA3_VERSION 2.5.0
RUN wget https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-${ANACONDA3_VERSION}-Linux-x86_64.sh
RUN bash Anaconda3-2.5.0-Linux-x86_64.sh -p /opt/anaconda3 -b
RUN update-alternatives --install /usr/bin/python python /opt/anaconda3/bin/python3 100

#Boost
WORKDIR /tmp
ENV BOOST_VERSION 1.60.0
RUN git clone -b boost-${BOOST_VERSION} --recursive https://github.com/boostorg/boost.git
WORKDIR boost
RUN apt-get -y install libbz2-dev
ADD user-config.jam /root/
RUN sh bootstrap.sh
RUN ./b2 headers --prefix=/opt
RUN ./b2 install --prefix=/opt

#Boost.Numpy
WORKDIR /tmp
RUN git clone -b find_other_name_format_python_lib https://github.com/ar90n/Boost.NumPy.git
RUN mkdir Boost.NumPy/build
WORKDIR Boost.NumPy/build
RUN cmake -DBoost_NO_BOOST_CMAKE=ON ..
RUN make
RUN cp lib/libboost_numpy.so /opt/lib/
RUN cp -rf ../boost/ /opt/include/

#Halide
WORKDIR /tmp
RUN apt-get -y install libxml2 libpng16-dev libjpeg-dev zlib1g-dev libedit-dev llvm-3.7 llvm-3.7-dev clang-3.7 libgl1-mesa-dev libopenblas-dev
RUN git clone https://github.com/halide/Halide.git
RUN mkdir Halide/build
WORKDIR Halide/build
RUN cmake -DLLVM_BIN=`llvm-config-3.7 --bindir` -DLLVM_INCLUDE=`llvm-config-3.7 --includedir` -DLLVM_LIB=`llvm-config-3.7 --libdir` -DLLVM_VERSION=37 ..
RUN make
RUN cp ./lib/libHalide.so /opt/lib
RUN cp -rf ./include /opt

#Halide python
WORKDIR /tmp/Halide/python_bindings
RUN mkdir build
WORKDIR build
RUN cmake -DPYTHON_LIBRARY=/opt/anaconda3/lib/libpython3.5m.so -DPYTHON_INCLUDE_DIR=/opt/anaconda3/include/python3.5m  -DHALIDE_ROOT_DIR=../../build -DUSE_BOOST_NUMPY=ON ..
RUN make
RUN cp halide.so `python -c 'import site;print(site.getsitepackages()[0])'`

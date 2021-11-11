# Dockerfile for OpenCV with CUDA C++, Python 2.7 / 3.6 development 
# Pulling CUDA-CUDNN image from nvidia
FROM mlamarre/cuda9.2-opencv3.4.1-dev:master-5278797
MAINTAINER Mathieu Lamarre <mathieu.lamarre@gmail.com>

ENV SUITESPARSE_VERSION 5.3.0

WORKDIR /
RUN mkdir /temp \
&& wget -qq http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-${SUITESPARSE_VERSION}.tar.gz -O /temp/SuiteSparse-${SUITESPARSE_VERSION}.tar.gz\
&& wget -qq https://raw.githubusercontent.com/mlamarre/docker-cuda-opencv-suitesparse/master/SuiteSparse_config_MKL_TBB.patch -O /temp/SuiteSparse_config_MKL_TBB.patch\
&& tar -xzvf /temp/SuiteSparse-${SUITESPARSE_VERSION}.tar.gz\
&& cd SuiteSparse/SuiteSparse_config\
&& patch < /temp/SuiteSparse_config_MKL_TBB.patch\
&& cd /SuiteSparse\
&& rm -rf /temp \
&& make MKLROOT=/opt/conda/envs/ocvpy3 TBB="-ltbb -DSPQR_CONFIG=-DHAVE_TBB" INSTALL=/usr/local -j$(nproc) install\
&& cd /\
&& rm -rf SuiteSparse

RUN ldconfig -v
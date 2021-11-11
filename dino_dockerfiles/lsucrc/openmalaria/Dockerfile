#Version 1.1
#add the base image
FROM lsucrc/crcbase
MAINTAINER Jian Tao <jtao@cct.lsu.edu>

#install required packages
RUN  yum install -y gsl-devel xsd xerces-c-devel zlib-devel boost-devel
USER crcuser

#download the package
WORKDIR /model
RUN git clone https://github.com/SwissTPH/openmalaria.git

#compile
WORKDIR openmalaria
RUN cmake -f CMakeLists.txt  
RUN make -j 4
ENV PATH $PATH:/model/openmalaria

#run test case
WORKDIR /model/openmalaria/test
RUN python run.py

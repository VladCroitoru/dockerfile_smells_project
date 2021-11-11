FROM centos:7
# install dependencies
RUN yum install epel-release -y
RUN yum install gcc-c++ git cmake make gtest-devel hdf5-devel lz4-devel -y

# install flann library
COPY flann.tar.gz /root
RUN mkdir -p /root/flann/build
RUN cd /root/flann && tar -xzvf ../flann.tar.gz .
RUN cd /root/flann/build && cmake .. && make && make install

# create working directory
RUN mkdir -p /root/motionexp

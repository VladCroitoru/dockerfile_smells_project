FROM blacklabelops/centos:latest

RUN yum install -y cmake gcc-c++ bzip2-devel libaio-devel bison \
    zlib-devel snappy-devel gflags-devel readline-devel ncurses-devel \
    openssl-devel lz4-devel gdb git libcap-devel libatomic libzstd boost-devel && mkdir mysql

RUM yum install -y make epel-release libzstd-devel

ADD . mysql

WORKDIR mysql

RUN git submodule init && git submodule update

# RUN cmake . -DCMAKE_BUILD_TYPE=RelWithDebInfo -DWITH_SSL=system \
#     -DWITH_ZLIB=bundled -DMYSQL_MAINTAINER_MODE=0 -DENABLED_LOCAL_INFILE=1 \
#     -DENABLE_DTRACE=0 -DCMAKE_CXX_FLAGS="-march=native" && make -j16




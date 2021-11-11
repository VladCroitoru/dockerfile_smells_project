FROM centos:7
RUN yum install -y git gcc clang cmake make gcc-c++  python2  libpcap
RUN mkdir -p /usr/local/include/ && \
        cd /usr/local/include/ && \
        curl -O http://www.colm.net/files/ragel/ragel-6.9.tar.gz && \
        tar -zxf ragel-6.9.tar.gz && cd ragel-6.9 && ./configure && make && make install && \
        cd /usr/local/include/ && \
        curl -L -O https://dl.bintray.com/boostorg/release/1.65.1/source/boost_1_65_1.tar.gz && \
        tar -zxf boost_1_65_1.tar.gz && cd /usr/local/include/boost_1_65_1/tools/build && ./bootstrap.sh && ./b2 install --prefix=/usr/local/include/boost && \
        cd /usr/local/include/ && \
        git clone https://github.com/intel/hyperscan.git && \
        ln -s /usr/local/include/boost_1_65_1/boost /usr/local/include/hyperscan/include/boost && \
        mkdir /usr/local/include/hs && \
        cd /usr/local/include/hs && \
        cmake /usr/local/include/hyperscan
RUN cd /usr/local/include/hs && \
        cmake --build .
#RUN rm -f /usr/local/include/hs/bin/simplegrep && rm -f /usr/local/include/hs/bin/unit-hyperscan

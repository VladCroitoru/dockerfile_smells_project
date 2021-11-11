FROM nimbix/ubuntu-base

RUN sudo apt-get -y update
RUN sudo apt-get install -y software-properties-common
RUN sudo add-apt-repository -y ppa:george-edison55/cmake-3.x
RUN sudo apt-get -y update
RUN sudo apt-get install -y cmake
RUN sudo apt-get install -y doxygen
RUN sudo apt-get install -y openssl libssl-dev lcov

RUN sudo apt-get install -y curl
RUN sudo apt-get install -y autoconf
RUN sudo apt-get install -y libtool
RUN sudo apt-get install -y build-essential git

RUN wget -nc https://github.com/google/protobuf/archive/v3.0.2.tar.gz &&  tar -xvf v3.0.2.tar.gz && cd protobuf-3.0.2 && ./autogen.sh && ./configure && make && make install

RUN sudo apt-get install -y libprotoc8 pkg-config

RUN wget -nc https://github.com/protobuf-c/protobuf-c/archive/v1.2.1.tar.gz && tar -xvf v1.2.1.tar.gz && cd protobuf-c-1.2.1 && ./autogen.sh &&  ./configure CFLAGS="-O3 -DNDEBUG" CXXFLAGS="-O3 -DNDEBUG" && make && make install

RUN wget http://mirrors.kernel.org/ubuntu/pool/main/n/numactl/libnuma1_2.0.9~rc5-1ubuntu2_amd64.deb && dpkg -i libnuma1_2.0.9~rc5-1ubuntu2_amd64.deb
RUN wget http://mirrors.kernel.org/ubuntu/pool/main/n/numactl/libnuma-dev_2.0.9~rc5-1ubuntu2_amd64.deb && dpkg -i libnuma-dev_2.0.9~rc5-1ubuntu2_amd64.deb
RUN wget http://mirrors.kernel.org/ubuntu/pool/main/liba/libaio/libaio1_0.3.109-4_amd64.deb && dpkg -i libaio1_0.3.109-4_amd64.deb
RUN wget http://mirrors.kernel.org/ubuntu/pool/main/liba/libaio/libaio-dev_0.3.109-4_amd64.deb && dpkg -i libaio-dev_0.3.109-4_amd64.deb


RUN apt-get install -y libtool autoconf automake build-essential vim
RUN apt-get install -y ibverbs-utils rdmacm-utils infiniband-diags perftest
RUN apt-get install -y librdmacm-dev libibverbs-dev numactl libnuma-dev libaio-dev libevent-dev

RUN wget -nc https://developer.nvidia.com/compute/cuda/8.0/prod/local_installers/cuda-repo-ubuntu1604-8-0-local_8.0.44-1_amd64-deb -O /tmp/cuda.deb && dpkg -i /tmp/cuda.deb && apt-get -y update && apt-get install -y cuda

RUN echo "Version 3" > ~/Version

ADD ./NAE/help.html /etc/NAE/help.html

CMD /bin/bash

ARG OS_VER=16.04 
ARG DPDK_VER=17.08
FROM ubuntu:${OS_VER}
MAINTAINER Amir Zeidner

WORKDIR /

# Install prerequisite packages
RUN apt-get update && apt-get install -y \
libnl-route-3-200 \
libnuma-dev \
numactl \
libnuma1 \
unzip \
wget \
make \
gcc \
ethtool \
net-tools \
linux-headers-$(uname -r) \
&& rm -rf /var/lib/apt/lists/* 

# Download and install Mellanox drivers
ARG OS_VER
RUN wget http://www.mellanox.com/downloads/ofed/MLNX_EN-4.1-1.0.2.0/mlnx-en-4.1-1.0.2.0-ubuntu${OS_VER}-x86_64.tgz && tar -xvzf /mlnx-en-4.1-1.0.2.0-ubuntu${OS_VER}-x86_64.tgz
RUN dpkg -i $( ls /mlnx-en-4.1-1.0.2.0-ubuntu${OS_VER}-x86_64/DEBS/libibverbs* | grep -v dbg )
RUN dpkg -i $( ls /mlnx-en-4.1-1.0.2.0-ubuntu${OS_VER}-x86_64/DEBS/libmlx* | grep -v dbg )

# Download and compile DPDK
ARG DPDK_VER
RUN cd /usr/src/ &&  wget http://dpdk.org/browse/dpdk/snapshot/dpdk-${DPDK_VER}.zip && unzip dpdk-${DPDK_VER}.zip 
ENV DPDK_DIR=/usr/src/dpdk-${DPDK_VER}  DPDK_TARGET=x86_64-native-linuxapp-gcc DPDK_BUILD=$DPDK_DIR/$DPDK_TARGET
RUN cd $DPDK_DIR && sed -i 's/\(CONFIG_RTE_LIBRTE_MLX5_PMD=\)n/\1y/g' $DPDK_DIR/config/common_base
RUN cd $DPDK_DIR && make install T=$DPDK_TARGET DESTDIR=install

# Remove unnecessary packages and files
RUN rm -rf /tmp/* && rm -rf /mlnx-en-4.1-1.0.2.0-ubuntu${OS_VER}-x86_64/ && rm /mlnx-en-4.1-1.0.2.0-ubuntu${OS_VER}-x86_64.tgz && rm /usr/src/dpdk-${DPDK_VER}.zip

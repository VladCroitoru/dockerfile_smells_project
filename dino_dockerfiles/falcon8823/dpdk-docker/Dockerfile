FROM ubuntu:16.04

ARG DPDK_VERSION=16.11

# Install Required packages
RUN apt-get update -y \
    && apt-get install -y -q curl build-essential linux-headers-$(uname -r) \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
RUN curl -O http://fast.dpdk.org/rel/dpdk-${DPDK_VERSION}.tar.xz \
       && tar xJf dpdk-${DPDK_VERSION}.tar.xz -C /usr/local/src \
       && rm dpdk-${DPDK_VERSION}.tar.xz

ENV RTE_TARGET x86_64-native-linuxapp-gcc
ENV RTE_SDK /usr/local/src/dpdk-${DPDK_VERSION}

WORKDIR $RTE_SDK
RUN make install T=${RTE_TARGET} \
    && make -C examples/

ENV PATH "$PATH:$RTE_SDK/$RTE_TARGET/app"


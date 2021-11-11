FROM ubuntu:17.04

# Install necessary packages
RUN apt-get update && apt-get install -y \
    libglib2.0-dev \
    libgcrypt20-dev \
    zlib1g-dev \
    autoconf \
    automake \
    libtool \
    bison \
    flex \
    wget unzip python \ 
    libpixman-1-dev \
    libfdt-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# get and configure qemu source
RUN wget https://github.com/Xilinx/qemu/archive/xilinx-v2017.2.zip && unzip xilinx-v2017.2.zip
RUN cd qemu-xilinx-v2017.2 && ./configure --target-list="aarch64-softmmu,microblazeel-softmmu" --enable-fdt --disable-kvm --disable-xen

# Deploy qemu
RUN cd /qemu-xilinx-v2017.2 && make && make install
RUN mkdir /share_fs

# Network setting
EXPOSE 1440

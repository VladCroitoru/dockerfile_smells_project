FROM idein/cross-rpi:armv6

ENV DEBIAN_FRONTEND noninteractive
ARG RPI_TARGET=armv6-rpi-linux-gnueabihf

# Enable backport repositories to provide clang/llvm 6 for stretch
# For some strange reason, sudo does not work here...
USER root
RUN echo "deb http://ftp.debian.org/debian stretch-backports main" > /etc/apt/sources.list.d/stretch-backports.list \
    && echo "deb http://ftp.debian.org/debian stretch-backports-sloppy main" > /etc/apt/sources.list.d/stretch-backports-sloppy.list

USER idein
RUN sudo apt-get update \
 && sudo apt-get upgrade -y \
 && sudo apt-get install -y --no-install-recommends \
      sudo git wget curl bc \
      gcc g++ automake libtool build-essential pkg-config \
      make python \
      apt-utils ca-certificates devscripts unzip \
 && sudo apt-get install -y --no-install-recommends -t stretch-backports-sloppy \
      libarchive13 \
 && sudo apt-get install -y --no-install-recommends -t stretch-backports \
      cmake opencl-c-headers \
      clang-6.0 llvm-6.0-dev llvm-6.0 libclang1-6.0 libclang-6.0-dev \
 && sudo apt-get clean && sudo rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

ENV SYSROOT_CROSS ${HOME}/cross

# LLVM library and headers for linking (ARM version)
RUN wget -O /tmp/libllvm-6.0.deb http://mirrordirector.raspbian.org/raspbian/pool/main/l/llvm-toolchain-6.0/libllvm6.0_6.0.1-14.1+rpi1_armhf.deb \
 && wget -O /tmp/llvm-6.0-dev.deb http://mirrordirector.raspbian.org/raspbian/pool/main/l/llvm-toolchain-6.0/llvm-6.0-dev_6.0.1-14.1+rpi1_armhf.deb \
 && wget -O /tmp/llvm-6.0.deb http://mirrordirector.raspbian.org/raspbian/pool/main/l/llvm-toolchain-6.0/llvm-6.0_6.0.1-14.1+rpi1_armhf.deb \
 && dpkg-deb -x	/tmp/libllvm-6.0.deb ${SYSROOT_CROSS}/ \
 && dpkg-deb -x	/tmp/llvm-6.0-dev.deb ${SYSROOT_CROSS}/ \
 && dpkg-deb -x	/tmp/llvm-6.0.deb ${SYSROOT_CROSS}/ \
 && rm /tmp/libllvm-6.0.deb /tmp/llvm-6.0-dev.deb /tmp/llvm-6.0.deb \
 && touch ${HOME}/cross/usr/lib/llvm-6.0/bin/lli # create dummy file

RUN sed -i -e "s|/usr/lib|/home/idein/cross/usr/lib|p" /home/idein/cross/usr/lib/llvm-6.0/cmake/LLVMConfig.cmake

# Additional system libraryries required for linking LLVM
RUN wget -O /tmp/libtinfo6.deb http://mirrordirector.raspbian.org/raspbian/pool/main/n/ncurses/libtinfo6_6.2-1_armhf.deb \
 && wget -O /tmp/libncurses6.deb http://mirrordirector.raspbian.org/raspbian/pool/main/n/ncurses/libncurses6_6.2-1_armhf.deb \
 && wget -O /tmp/libzlib1g.deb http://mirrordirector.raspbian.org/raspbian/pool/main/z/zlib/zlib1g_1.2.11.dfsg-2_armhf.deb \
 && wget -O /tmp/libffi7.deb http://mirrordirector.raspbian.org/raspbian/pool/main/libf/libffi/libffi7_3.3-4_armhf.deb \
 && wget -O /tmp/libffi7-dev.deb http://mirrordirector.raspbian.org/raspbian/pool/main/libf/libffi/libffi-dev_3.3-4_armhf.deb \
 && wget -O /tmp/libedit2.deb http://mirrordirector.raspbian.org/raspbian/pool/main/libe/libedit/libedit2_3.1-20191231-1_armhf.deb \
 && wget -O /tmp/libedit2-dev.deb http://mirrordirector.raspbian.org/raspbian/pool/main/libe/libedit/libedit-dev_3.1-20191231-1_armhf.deb \
 && wget -O /tmp/libbsd.deb http://mirrordirector.raspbian.org/raspbian/pool/main/libb/libbsd/libbsd0_0.10.0-1_armhf.deb \
 && dpkg-deb -x /tmp/libtinfo6.deb ${SYSROOT_CROSS}/ \
 && dpkg-deb -x /tmp/libncurses6.deb ${SYSROOT_CROSS}/ \
 && dpkg-deb -x /tmp/libzlib1g.deb ${SYSROOT_CROSS}/ \
 && dpkg-deb -x /tmp/libffi7.deb ${SYSROOT_CROSS}/ \
 && dpkg-deb -x /tmp/libffi7-dev.deb ${SYSROOT_CROSS}/ \
 && dpkg-deb -x /tmp/libedit2.deb ${SYSROOT_CROSS}/ \
 && dpkg-deb -x /tmp/libedit2-dev.deb ${SYSROOT_CROSS}/ \
 && dpkg-deb -x /tmp/libbsd.deb ${SYSROOT_CROSS}/ \
 && rm /tmp/libtinfo6.deb /tmp/libncurses6.deb /tmp/libzlib1g.deb /tmp/libffi7.deb /tmp/libffi7-dev.deb /tmp/libedit2.deb /tmp/libedit2-dev.deb /tmp/libbsd.deb

RUN wget -O /tmp/ocl-icd-opencl-dev.deb http://mirrordirector.raspbian.org/raspbian/pool/main/o/ocl-icd/ocl-icd-opencl-dev_2.2.12-4_armhf.deb \
 && wget -O /tmp/ocl-icd-libopencl1.deb http://mirrordirector.raspbian.org/raspbian/pool/main/o/ocl-icd/ocl-icd-libopencl1_2.2.12-4_armhf.deb \
 && wget -O /tmp/opencl-c-headers.deb http://mirrordirector.raspbian.org/raspbian/pool/main/k/khronos-opencl-headers/opencl-c-headers_2.1-1_all.deb \
 && wget -O /tmp/ocl-icd-dev.deb http://mirrordirector.raspbian.org/raspbian/pool/main/o/ocl-icd/ocl-icd-dev_2.2.12-4_armhf.deb \
 && dpkg-deb -x /tmp/ocl-icd-opencl-dev.deb ${SYSROOT_CROSS}/ \
 && dpkg-deb -x /tmp/ocl-icd-libopencl1.deb ${SYSROOT_CROSS}/ \
 && dpkg-deb -x /tmp/opencl-c-headers.deb ${SYSROOT_CROSS}/ \
 && dpkg-deb -x /tmp/ocl-icd-dev.deb ${SYSROOT_CROSS}/ \
 && rm /tmp/*.deb

# Additional packages required to fulfill dependencies
RUN wget -O /tmp/libncurses-dev.deb http://mirrordirector.raspbian.org/raspbian/pool/main/n/ncurses/libncurses-dev_6.2-1_armhf.deb \
 && dpkg-deb -x /tmp/libncurses-dev.deb ${SYSROOT_CROSS}/ \
 && rm /tmp/libncurses-dev.deb

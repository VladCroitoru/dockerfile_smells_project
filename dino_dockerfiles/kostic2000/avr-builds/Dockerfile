##
## GCC AVR Toolchain, simavr, host gcc toolchain

FROM ubuntu:latest
MAINTAINER Konstantin Begun

ENV GCC_VERSION 6.3.0
ENV LIBC_VERSION 2.0.0
ENV BINUTILS_VERSION 2.28

RUN \
    #### install build tools ####
    apt-get update && apt-get install -y --no-install-recommends \
                              wget                               \
			      git				 \
                              build-essential                    \
			      pkg-config			 \
                              libmpc-dev                         \
                              libmpfr-dev                        \
                              libgmp3-dev                        \
			      libelf-dev			 \
			      freeglut3-dev			 \
 && mkdir /opt/distr && cd /opt/distr \
    #### build and install cmake-3.3.2 ####
 && wget https://cmake.org/files/v3.3/cmake-3.3.2.tar.gz --no-check-certificate \
 && tar -zxvf cmake-3.3.2.tar.gz && cd cmake-3.3.2 \
 && ./bootstrap && make && make install && cd .. \
    #### build and install make-4.2.1 ####
 && wget http://ftp.gnu.org/gnu/make/make-4.2.1.tar.bz2 \
 && bunzip2 -c make-4.2.1.tar.bz2 | tar xf - && cd make-4.2.1 \
 && mkdir build && cd build \
 && ../configure \
 && make && make install && cd ../.. \
    #### build and install binutils-2.25.1 ####
 && wget http://ftp.gnu.org/gnu/binutils/binutils-$BINUTILS_VERSION.tar.bz2 \
 && bunzip2 -c binutils-$BINUTILS_VERSION.tar.bz2 | tar xf - && cd binutils-$BINUTILS_VERSION \
 && mkdir build && cd build \
 && ../configure --target=avr --disable-nls \
 && make && make install && cd ../.. \
    #### build and install gcc####
 && wget http://mirrors-usa.go-parts.com/gcc/releases/gcc-$GCC_VERSION/gcc-$GCC_VERSION.tar.bz2 \
 && bunzip2 -c gcc-$GCC_VERSION.tar.bz2 | tar xf - && cd gcc-$GCC_VERSION \
 && mkdir build && cd build \
 && ../configure --target=avr --enable-languages=c,c++ --disable-nls --disable-libssp --with-dwarf2 \
 && make && make install && cd ../.. \
    #### build and install libc####
 && wget http://download.savannah.gnu.org/releases/avr-libc/avr-libc-$LIBC_VERSION.tar.bz2 \
 && bunzip2 -c avr-libc-$LIBC_VERSION.tar.bz2 | tar xf - && cd avr-libc-$LIBC_VERSION \
 && ./configure --build=`./config.guess` --host=avr \
 && make && make install && cd .. \
	#### build and install simavr ####
 && git clone git://github.com/kostic2000/simavr.git \
 && cd simavr \
 && make && make install && cd .. \
    #### clean up the image ####
 && cd .. && rm -rf distr   \
 && apt-get autoremove -y   \
 && apt-get clean           \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 && ldconfig


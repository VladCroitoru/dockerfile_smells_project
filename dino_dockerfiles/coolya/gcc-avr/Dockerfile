##
## Toolchain and tools to build AVR projects with C/C++ and Assembler.

FROM ubuntu:latest
MAINTAINER Kolja Dummann <kolja.dummann@logv.ws>

ENV GCC_VERSION 7.1.0
ENV LIBC_VERSION 2.0.0
ENV BINUTILS_VERSION 2.29
ENV CMAKE_VERSION 3.3.2

ENV PATH $PATH:/usr/local/avr/bin

RUN \
    #### install build tools ####
    apt-get update && apt-get install -y --no-install-recommends \
                              wget                               \
                              make                               \
                              build-essential                    \
                              libmpc-dev                         \
                              libmpfr-dev                        \
                              libgmp3-dev                        \
 && mkdir /usr/local/avr /opt/distr && cd /opt/distr \
    #### build and install cmake-3.3.2 ####
 && wget https://cmake.org/files/v3.3/cmake-$CMAKE_VERSION.tar.gz --no-check-certificate \
 && tar -zxvf cmake-$CMAKE_VERSION.tar.gz && cd cmake-$CMAKE_VERSION \
 && ./bootstrap && make -j$(nproc --all)  && make install && cd .. \
    #### build and install binutils-2.25.1 ####
 && wget http://ftp.gnu.org/gnu/binutils/binutils-$BINUTILS_VERSION.tar.bz2 \
 && bunzip2 -c binutils-$BINUTILS_VERSION.tar.bz2 | tar xf - && cd binutils-$BINUTILS_VERSION \
 && mkdir build && cd build \
 && ../configure --prefix=/usr/local/avr --target=avr --disable-nls \
 && make -j$(nproc --all)  && make install && cd ../.. \
    #### build and install gcc####
 && wget http://mirrors.concertpass.com/gcc/releases/gcc-$GCC_VERSION/gcc-$GCC_VERSION.tar.gz \
 &&  tar -zxvf gcc-$GCC_VERSION.tar.gz && cd gcc-$GCC_VERSION \
 && mkdir build && cd build \
 && ../configure --prefix=/usr/local/avr --target=avr --enable-languages=c,c++ --disable-nls --disable-libssp --with-dwarf2 \
 && make -j$(nproc --all)  && make install && cd ../.. \
    #### build and install libc####
 && wget http://download.savannah.gnu.org/releases/avr-libc/avr-libc-$LIBC_VERSION.tar.bz2 \
 && bunzip2 -c avr-libc-$LIBC_VERSION.tar.bz2 | tar xf - && cd avr-libc-$LIBC_VERSION \
 && ./configure --prefix=/usr/local/avr --build=`./config.guess` --host=avr \
 && make -j$(nproc --all)  && make install && cd .. \
    #### clean up the image ####
 && cd .. && rm -rf distr   \
 && apt-get remove -y       \
            wget            \
            build-essential \
 && apt-get autoremove -y   \
 && apt-get clean           \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


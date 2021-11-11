FROM ubuntu:16.04

RUN apt-get update -qq

RUN apt-get install -qy build-essential git curl libtool libjansson* libssl-dev libcurl4-openssl-dev libncurses5-dev libgmp-dev automake

RUN git clone https://github.com/JayDDee/cpuminer-opt -b legacy

RUN cd cpuminer-opt \
    && ./autogen.sh \
    && ./configure CFLAGS="-O3 -msse4.1" CXXFLAGS="$CFLAGS -std=gnu++11" --with-curl --with-crypto \
    && make \
    && make install

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -qy nodejs

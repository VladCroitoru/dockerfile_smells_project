FROM ubuntu:14.04

RUN apt-get update && apt-get install -y g++ build-essential autoconf automake automake1.9 cmake doxygen bison flex libncurses5-dev libsdl1.2-dev libreadline-dev libusb-dev texinfo libgmp3-dev libmpfr-dev libelf-dev libmpc-dev libfreetype6-dev zlib1g-dev libtool libtool subversion git tcl unzip wget

RUN mkdir -p /data/psptoolchain

ADD . /data/psptoolchain

WORKDIR /data/psptoolchain

RUN ./toolchain-sudo.sh && ./toolchain-sudo.sh clean

ENV PATH="$PATH:/usr/local/pspdev/bin/"

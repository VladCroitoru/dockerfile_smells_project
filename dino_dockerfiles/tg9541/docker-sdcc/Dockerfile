FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y curl subversion build-essential flex bison libboost-dev \
       texinfo stx-btree-dev zip netcat gawk python3 python3-serial libz-dev telnet vim \
    && apt-get autoclean

RUN mkdir /sdcc -p \
    && cd /sdcc \
    && svn checkout svn://svn.code.sf.net/p/sdcc/code/trunk/sdcc@11214 \
    && cd sdcc \
    && ./configure --disable-pic14-port --disable-pic16-port \
                   --disable-pdk-port --disable-z80-port \
                   --disable-mcs51-port --disable-h08-port \
                   --disable-ds390-port --disable-avr-port \
    && make && make install \
    && cd / \
    && rm -Rf /sdcc /tmp/*

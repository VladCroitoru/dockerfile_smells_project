# VBCC Installation tutorial for Amiga m68k from https://www.youtube.com/watch?v=vFV0oEyY92I

FROM debian:jessie
MAINTAINER Ozzyboshi <gun101@email.it>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y install gcc wget curl make lhasa


WORKDIR /root
RUN mkdir vbcc_tools && mkdir -p amiga_sdk/vbcc

WORKDIR /root/vbcc_tools
RUN wget http://server.owl.de/~frank/tags/vbcc0_9f.tar.gz && \
	wget http://server.owl.de/~frank/vbcc/2016-03-23/vbcc_target_m68k-amigaos.lha && \
	wget http://server.owl.de/~frank/vbcc/2015-11-22/vbcc_target_m68k-amigaos_P2.lha && \
	wget http://server.owl.de/~frank/vbcc/2016-03-23/vbcc_unix_config.tar.gz && \
	wget http://server.owl.de/~frank/vbcc/2015-06-04/vbcc_target_m68k-amigaos-v4.lha

RUN tar xvfz vbcc0_9f.tar.gz && cd vbcc && mkdir bin && yes '\
' | make TARGET=m68k && cp -r bin ~/amiga_sdk/vbcc/
RUN lha x vbcc_target_m68k-amigaos.lha && cp -r vbcc_target_m68k-amigaos/* ~/amiga_sdk/vbcc
WORKDIR /root/amiga_sdk/vbcc
RUN lha x ~/vbcc_tools/vbcc_target_m68k-amigaos-v4.lha
RUN lha xf ~/vbcc_tools/vbcc_target_m68k-amigaos_P2.lha
RUN tar xvfz ~/vbcc_tools/vbcc_unix_config.tar.gz
ENV VBCC="/root/amiga_sdk/vbcc"
ENV PATH="$VBCC/bin:${PATH}"
RUN wget http://sun.hasenbraten.de/vasm/release/vasm.tar.gz && tar xvfz vasm.tar.gz && cd vasm && make CPU=m68k SYNTAX=mot && cp vasmm68k_mot vobjdump $VBCC/bin
RUN wget http://sun.hasenbraten.de/vlink/release/vlink.tar.gz && tar xvfz vlink.tar.gz && cd vlink && mkdir objects && make && cp vlink $VBCC/bin
WORKDIR /root/amiga_sdk
RUN wget http://www.haage-partner.de/download/AmigaOS/NDK39.lha && lha x NDK39.lha
ENV NDK_INC=/root/amiga_sdk/NDK_3.9/Include/include_h
WORKDIR /root
CMD /root/amiga_sdk/vbcc/bin/vc

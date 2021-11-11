FROM ubuntu:16.04

LABEL maintainer "patrick.grosse@uni-muenster.de"

RUN DEBIAN_FRONTEND=noninteractive apt-get update -q && apt-get install -yqq sudo bzip2 wget build-essential unzip libevent-dev gcc-multilib cmake git curl

# gcc arm none eabi
RUN wget --quiet https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu-rm/6-2016q4/gcc-arm-none-eabi-6_2-2016q4-20161216-linux.tar.bz2 && \
	tar xjf gcc-arm-none-eabi-6_2-2016q4-20161216-linux.tar.bz2 && \
	rm gcc-arm-none-eabi-6_2-2016q4-20161216-linux.tar.bz2
ENV PATH "$PATH:/gcc-arm-none-eabi-6_2-2016q4/bin"

# libcoap
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yqq asciidoc automake pkg-config libtool && \
	git clone https://github.com/obgm/libcoap.git && \
	cd libcoap && \
	./autogen.sh && \
	./configure && \
	make && \
	sudo make install && \
	apt-get remove -yqq --auto-remove asciidoc && \
	cd .. && \
	rm -rf libcoap

FROM ubuntu:xenial

MAINTAINER Carlos Ortigoza "carlos.ortigoza@ungleich.ch"

WORKDIR /root

RUN apt-get update -y && \
	apt-get install -y git gcc binutils make perl syslinux liblzma-dev genisoimage isolinux && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* && \
	git clone git://git.ipxe.org/ipxe.git

RUN cd /root/ipxe/src && make bin/ipxe.iso

COPY ipxe_script_builder.sh /root

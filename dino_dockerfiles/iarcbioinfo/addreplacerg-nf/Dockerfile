# Set the base image to Debian
FROM debian:latest

# File Author / Maintainer
MAINTAINER Matthieu Foll <follm@iarc.fr>

RUN apt-get clean && \
	apt-get update -y && \

	# Install dependences
	DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
	g++ \
	make \
	zlib1g-dev \
	libncurses5-dev \
	ca-certificates \
	dialog \
	wget \
	bzip2 && \

	# Install samtools 
	wget https://github.com/samtools/samtools/releases/download/1.3/samtools-1.3.tar.bz2 && \
	tar -jxf samtools-1.3.tar.bz2 && \
	cd samtools-1.3 && \
	make && \
	make install && \
	cd .. && \
	rm -rf samtools-1.3 samtools-1.3.tar.bz2 && \

	# Remove unnecessary dependences
	DEBIAN_FRONTEND=noninteractive apt-get remove -y \
	g++ \
	make \
	zlib1g-dev \
	libncurses5-dev \
	dialog \
	wget \
	bzip2 \
	software-properties-common && \

	# Clean
	DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \ 
	apt-get clean
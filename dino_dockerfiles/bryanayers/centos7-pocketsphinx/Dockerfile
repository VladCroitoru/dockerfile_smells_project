# Base OS
FROM centos:7
MAINTAINER bryanayers+Dockerfile@gmail.com

# Env setup
ENV HOME /root
ENV LD_LIBRARY_PATH=/usr/local/lib
ENV PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
WORKDIR ~/

# Build deps
RUN \
	yum -y update &&\
	yum -y install epel-release &&\
	yum -y install \
		autoconf \
		automake \
		bison \
		bzip2 \
		gcc-c++ \
		libtool \
		libuuid-devel \
		make \
		pulseaudio pulseaudio-libs pulseaudio-libs-devel pulseaudio-utils \
		python python-devel python-libs \
		swig \
		tar \
		wget && \
	yum clean all

RUN \
	wget http://downloads.sourceforge.net/project/cmusphinx/sphinxbase/5prealpha/sphinxbase-5prealpha.tar.gz &&\
	wget http://downloads.sourceforge.net/project/cmusphinx/pocketsphinx/5prealpha/pocketsphinx-5prealpha.tar.gz &&\

	tar -xzf sphinxbase-5prealpha.tar.gz &&\
	tar -xzf pocketsphinx-5prealpha.tar.gz &&\

	cd sphinxbase-5prealpha &&\
	./configure &&\
	make &&\
	make install &&\

	cd ../pocketsphinx-5prealpha &&\
	./configure &&\
	make &&\
	make install &&\

	cd .. &&\

	# Cleanup
	rm -Rf sphinxbase* &&\
	rm -Rf pocketsphinx* &&\
	rm -Rf *.tar.*

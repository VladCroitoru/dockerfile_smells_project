# Base OS
FROM centos:7
MAINTAINER info@incendonet.com

# Env setup
ENV \
	HOME="/root" \
	SRC="/usr/local/src" \
	SIPP_VER="3.5.1"
WORKDIR ~/

# Get updates and build deps
RUN \
	yum -y update &&\
	yum -y install \
		autoconf \
		automake \
		gcc \
		gcc-c++ \
		less \
		libpcap-devel \
		libtool \
		lksctp-tools-devel \
		make \
		ncurses-devel \
		openssl-devel \
		wget &&\
	yum clean all

# Install SIPp
RUN \
	cd $SRC/ &&\

	wget https://github.com/SIPp/sipp/releases/download/v${SIPP_VER}/sipp-${SIPP_VER}.tar.gz &&\
	tar -xzf sipp-${SIPP_VER}.tar.gz &&\
	cd sipp-${SIPP_VER} &&\
	./configure --with-openssl --with-pcap --with-rtpstream --with-sctp &&\
	make &&\
	make install &&\
	cd .. &&\
	rm -Rf sipp-${SIPP_VER} sipp-${SIPP_VER}.tar.gz

EXPOSE 5060
# Port 8888 intentionally not exposed

CMD ["sipp"]

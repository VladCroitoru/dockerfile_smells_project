#
# Docker container for building SipX packages
#

FROM centos:centos6
MAINTAINER SIPFoundry Dev <sipfoundrydev@gmail.com>

#
# Install EPEL repository
#
RUN yum -y update; yum -y install epel-release; yum clean all; yum -y --disablerepo=epel update  ca-certificates
#RUN sed -i "s/#baseurl/baseurl/" /etc/yum.repos.d/epel.repo; sed -i "s/mirrorlist/#mirrorlist/" /etc/yum.repos.d/epel.repo

#
# Install Dependency Package
#

RUN yum -y install \
	automake \
	bison \
	bind-utils \
	bzip2-devel \
	boost-devel \
	chrpath \
	cppunit-devel \
	createrepo \
	db4-devel \
	elfutils-devel \
	elfutils-libelf-devel \
	findutils \
	flex \
	gcc-c++ \
	git \
	gperftools-devel \
	gtest-devel \
	hiredis-devel \
	httpd-devel \
	iproute \
	iptables \
	leveldb-devel \
	libacl-devel \
	libconfig-devel \
	libdnet-devel \
	libevent-devel \
	libmcrypt-devel \
	libpcap-devel \
	libtool \
	libtool-ltdl \
	libtool-ltdl-devel \
	libselinux-devel \
	libsrtp-devel \
	libtool \
	libtool-ltdl-devel \
	lksctp-tools-devel \
	lm_sensors-devel \
	m4 \
	mongoose \
	mysql-devel \
	net-tools \
	openssh-clients \
	openssl-devel \
	patch \
	pcre-devel \
	perl \
	perl-devel \
	perl-TAP-Harness-Archive \
	perl-TAP-Harness-JUnit \
	perl-ExtUtils-Embed \
	poco-devel \
	postgresql-devel \
	python-devel \
	python-setuptools \
	rpm-build \
	rpm-devel \
	ruby \
	ruby-devel \
	rubygem-mocha \
	rubygem-rake \
	rubygems \
	shadow-utils \
	scons \
	tar \
	tcp_wrappers-devel \
	tetex-dvips \
	texinfo-tex \
	tokyocabinet-devel \
	unixODBC-devel \
	vixie-cron \
	v8-devel \
	xerces-c-devel \
	xmlrpc-c-devel \
	zeromq-devel \
	zip \
	;

#
# Clean up
#
RUN yum clean all



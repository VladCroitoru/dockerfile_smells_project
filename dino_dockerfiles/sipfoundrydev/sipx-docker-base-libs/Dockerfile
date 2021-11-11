#
# Docker container for building SipX packages
#

FROM sipfoundrydev/sipx-docker-base-image:latest
MAINTAINER SIPFoundry Dev <sipfoundrydev@gmail.com>

#
# Add the repository for sipx-baselibs
#
ADD sipx-baselibs.repo /etc/yum.repos.d/

#
# Update the yum database
#
RUN yum -y clean all; yum -y update

#
# Install Dependency Packages
#

RUN yum -y install \
	cfengine \
	dart-sdk \
	mongo-cxx-driver-devel \
	mongodb \
	mongodb-server \
	net-snmp \
	net-snmp-agent-libs \
	net-snmp-devel \
	net-snmp-gui \
	net-snmp-libs \
	net-snmp-perl \
	net-snmp-python \
	net-snmp-sysvinit \
	net-snmp-utils \
	ruby-dbi \
	rubygem-file-tail \
	rubygem-net-sftp \
	rubygem-net-ssh \
	ruby-postgres
	
#
# Install packages needed by FreeSWITCH
#
RUN yum install -y \
	gnutls-devel \
	speex-devel \
	sqlite-devel \
	ldns-devel \
	libedit-devel \
	libmemcached-devel \
	libogg-devel \
	libvorbis-devel \
	libjpeg-devel \
	alsa-lib-devel \
	e2fsprogs-devel \
	libtheora-devel \
	portaudio-devel \
	libX11-devel \
	erlang \
	unixODBC-devel \
	lzo-devel \
	openssl098e \
	which

#
# Install Kamailio dependencies
#
RUN yum -y install \
	kamailio \
	kamailio-mongodb \
	kamailio-mysql \
	kamailio-presence \
	kamailio-sipx \
	redis \
	redhat-rpm-config \
	libev-devel \
	lksctp-tools-devel \
	mongo-c-driver-devel \
	mysql-server

#
# Do the final yum cleanup
#	
RUN yum -y clean all





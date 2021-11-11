#
# Docker container for building SipX packages
#

FROM sipfoundrydev/sipx-docker-base-libs:latest
MAINTAINER SIPFoundry Dev <sipfoundrydev@gmail.com>

#
# Add the repository for sipx
#
ADD sipx-baselibs.repo /etc/yum.repos.d/
ADD sipx-router.repo /etc/yum.repos.d/

#
# Update the yum database
#
RUN yum -y clean all; yum -y update

#
# Install Dependency Packages
#

RUN yum -y install \
	bind \
	cfengine \
	chkconfig \
	dart-sdk \
	dejavu-serif-fonts \
	dhcp \
	fail2ban \
	fontconfig \
	freeswitch \
	httpd \
	java-1.7.0-openjdk \
	java-1.7.0-openjdk-devel \
	js \
	libxslt \
	make \
	mod_ssl \
	mongodb \
	mongodb-server \
	net-snmp \
	net-snmp-agent-libs \
	net-snmp-devel \
	net-snmp-libs \
	net-snmp-python \
	net-snmp-sysvinit \
	net-snmp-utils \
	ntp \
	oss_core \
	pcre-devel \
	policycoreutils \
	postgresql-odbc \
	postgresql-server \
	python-argparse \
	python-pymongo \
	rsync \
	ruby \
	ruby-dbi \
	ruby-devel \
	rubygem-net-sftp \
	rubygems \
	ruby-libs \
	ruby-postgres \
	sec \
	sendmail \
	sendmail-cf \
	shadow-utils \
	sipxcommserverlib \
	sipxtacklib \
	sipXproxy \
	sipXregistry \
	sipXtools \
	stunnel \
	system-config-network-tui \
	tftp-server \
	unixODBC-devel \
	vixie-cron \
	vsftpd \
	which \
	zip



#
# Do the final yum cleanup
#	
RUN yum -y clean all





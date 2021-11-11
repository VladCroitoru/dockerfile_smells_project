#
# Docker container for building SipX packages
#

FROM sipfoundrydev/sipx-docker-router-libs:latest
MAINTAINER SIPFoundry Dev <sipfoundrydev@gmail.com>

#
# Add the repository for sipx
#
ADD sipx-baselibs.repo /etc/yum.repos.d/
ADD sipx-router.repo /etc/yum.repos.d/
ADD sipx-config.repo /etc/yum.repos.d/

#
# Update the yum database
#
RUN yum -y clean all; yum -y update

#
# Install Dependency Packages
#

RUN yum -y install \
	sipxsupervisor \
	sipxcommons \
	sipxcdr \
	sipxcdr-client \
	sipxconfig \
	sipxconfig-ftp \
	sipxconfig-tftp \
	sipxviewer \
	sipxrest \
	sipxcallcontroller \
	sipxcdrlog \
	sipxprovision


#
# Do the final yum cleanup
#	
RUN yum -y clean all





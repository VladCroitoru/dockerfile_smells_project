ARG CENTOS_VERSION=7.3.1611
FROM centos:${CENTOS_VERSION}

MAINTAINER ZeroC0D3 Team <zeroc0d3.team@gmail.com>

#-----------------------------------------------------------------------------
# Set Environment
#-----------------------------------------------------------------------------
ENV S6OVERLAY_VERSION=1.21.4.0 \
    S6_BEHAVIOUR_IF_STAGE2_FAILS=1 \
    LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    TERM=xterm

#-----------------------------------------------------------------------------
# Base Install + Import the RPM GPG keys for Repositories
#-----------------------------------------------------------------------------
RUN rpm --rebuilddb \
	  && rpm --import \
		   http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7 \
	  && rpm --import \
		   https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7 \
	  && rpm --import \
		   https://dl.iuscommunity.org/pub/ius/IUS-COMMUNITY-GPG-KEY

#-----------------------------------------------------------------------------
# Install Core Packages
#-----------------------------------------------------------------------------
RUN yum makecache fast \
    && yum provides '*/applydeltarpm' \
    && yum -y install \
              --setopt=tsflags=nodocs \
              --disableplugin=fastestmirror \
            deltarpm \
            bash-completion \
            epel-release \
            initscripts \
            sudo

#-----------------------------------------------------------------------------
# Update & Install Base Dependency
#-----------------------------------------------------------------------------
RUN yum -y update \
    && yum -y install iproute \
            open-ssl \
            openssl-libs \
            net-tools \
            gawk \
            bind-utils \
            bash \
            ca-certificates \
            curl \
            wget \
            tar \
            ansible \
            openssh \
            openssh-clients \
            openssh-server \
            python-pip \
            sudo \
            which \
            mc \
            nmap \
            supervisor \
            xz \
            nano \
            zip \
            unzip \

    && curl -sSL https://github.com/just-containers/s6-overlay/releases/download/v${S6OVERLAY_VERSION}/s6-overlay-amd64.tar.gz | tar xz -C / \

#-----------------------------------------------------------------------------
# Clean Up All Cache
#-----------------------------------------------------------------------------
    && yum clean all

#-----------------------------------------------------------------------------
# Setup Locale UTF-8
#-----------------------------------------------------------------------------
RUN ["/usr/bin/localedef", "-i", "en_US", "-f", "UTF-8", "en_US.UTF-8"]

#-----------------------------------------------------------------------------
# Symlink bash & sh (Inside Container)
#-----------------------------------------------------------------------------
RUN ["ln", "-s", "/usr/bin/bash", "/bin/bash"]
RUN ["ln", "-s", "/usr/bin/sh", "/bin/sh"]

#-----------------------------------------------------------------------------
# Finalize (reconfigure)
#-----------------------------------------------------------------------------
COPY rootfs/ /

FROM centos:7

# Need root to build image
USER root

# install dev tools
RUN yum install -y \
      unzip \
      tar \
      gzip \
      wget

# install Hashicorp tools
RUN export VAGRANT_VERSION=2.0.0 && \
    wget --directory-prefix=/tmp https://releases.hashicorp.com/vagrant/${VAGRANT_VERSION}/vagrant_${VAGRANT_VERSION}_x86_64.rpm && \
    rpm -i /tmp/vagrant_${VAGRANT_VERSION}_x86_64.rpm

# install ansible
RUN yum install ansible -y

# install Virtualbox (Example version: 5.1)
RUN export VIRTUALBOX_VERSION=latest && \
    mkdir -p /opt/virtualbox && \
    cd /etc/yum.repos.d/ && \
    wget http://download.virtualbox.org/virtualbox/rpm/el/virtualbox.repo && \
    yum install -y \
      dkms \
      kernel-devel && \
    yum -y groupinstall "Development Tools" && \
    if  [ "${VIRTUALBOX_VERSION}" = "latest" ]; \
      then yum install -y VirtualBox-5.1 ; \
      else yum install -y VirtualBox-5.1-${VIRTUALBOX_VERSION} ; \
    fi && \
    yum clean all && rm -rf /var/cache/yum/* && rm -rf /tmp/*

RUN vagrant plugin install vagrant-vbguest

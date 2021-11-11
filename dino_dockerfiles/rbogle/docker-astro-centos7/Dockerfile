FROM centos:7

RUN yum update -y && yum -y install epel-release
RUN yum install -y \
  curl \
  git \
  initscripts \
  openssh-server \
  openssh-clients \
  subversion \
  sudo \
  which \
  wget \
  unzip \
  zip \
  && yum clean all
RUN update-ca-trust enable
ADD http://sslhelp.doi.net/docs/DOIRootCA2.cer /etc/pki/ca-trust/source/anchors/
RUN update-ca-trust extract

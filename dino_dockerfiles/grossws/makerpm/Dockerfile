FROM centos:7
MAINTAINER Konstantin Gribov <grossws@gmail.com>

ENV UPDATED_AT 2015120500

RUN yum update -y \
  && yum groups install -y @development \
  && yum install -y epel-release \
  && yum install -y git mercurial subversion cvs \
  && yum install -y rpmdevtools rpmlint createrepo mock yum-utils \
  && yum clean all \
  && useradd --gid users --create-home --home-dir /makerpm makerpm

COPY makerpm.sh /makerpm.sh

ENTRYPOINT ["/makerpm.sh"]


FROM centos:centos7

MAINTAINER Russ Ferriday "russf@topia.com"

RUN yum -y update && yum -y groupinstall 'Development Tools' && yum -y install \
    bzip2-devel \
    glib2-devel \
    libcurl \
    libcurl-devel \
    libevent-devel \
    libffi-devel \
    libjpeg-devel \
    libxml2-devel \
    libxslt-devel \
    ncurses-devel \
    openssl \
    openssl-devel \
    postgresql-devel \
    mysql-devel \
    readline \
    readline-devel \
    sqlite-devel \
    wget \
    && yum clean all

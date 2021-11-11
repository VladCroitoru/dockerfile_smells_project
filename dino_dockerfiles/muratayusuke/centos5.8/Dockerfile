FROM tianon/centos:5.8
MAINTAINER Yusuke Murata <info@muratayusuke.com>

ENV LANG C.UTF-8

# install chef
RUN yum -y install curl
RUN curl -L https://www.opscode.com/chef/install.sh | bash

# install berkshelf
RUN yum -yv install gcc44-c++
RUN yum -yv install make
RUN yum -yv install diffutils
RUN yum -yv install perl
RUN yum -yv install autoconf
RUN ln -s /usr/bin/gcc44 /usr/bin/gcc
RUN ln -s /usr/bin/g++44 /usr/bin/g++
RUN /opt/chef/embedded/bin/gem install berkshelf --no-ri --no-rdoc

# Creating a Docker container containing Chef Client 12.x
#
# https://www.chef.io/download-chef-client/
#
FROM centos:7

MAINTAINER Ken Jenney <me@kenjenney.com>

RUN yum -y update
RUN yum -y install curl 
RUN curl -L https://www.chef.io/chef/install.sh | bash -s --
RUN yum clean all

# Make Chef available as a volume
VOLUME /opt/chef

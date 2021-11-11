# This file creates a container that contains chef-client and berkshelf
#
# Author: Paul Czarkowski
# Date: 08/04/2013


FROM ubuntu:14.04
MAINTAINER Paul Czarkowski "paul@paulcz.net"

RUN apt-get -yqq update \
  && apt-get -yqq install curl build-essential libxml2-dev libxslt-dev git autoconf

RUN curl -L https://www.opscode.com/chef/install.sh \
  | bash > /dev/null
  
RUN /opt/chef/embedded/bin/gem install berkshelf > /dev/null

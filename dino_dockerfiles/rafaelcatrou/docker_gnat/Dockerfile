# --------------------------------------------------------------------------------------------------
# LICENSE
# --------------------------------------------------------------------------------------------------
# ! # License #
# ! Copyright 2016 Rafael CATROU
# !
# ! Licensed under the Apache License, Version 2.0 (the "License");
# ! you may not use this file except in compliance with the License.
# ! You may obtain a copy of the License at
# !
# !     http://www.apache.org/licenses/LICENSE-2.0
# !
# ! Unless required by applicable law or agreed to in writing, software
# ! distributed under the License is distributed on an "AS IS" BASIS,
# ! WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# ! See the License for the specific language governing permissions and
# ! limitations under the License.
# !
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Base OS + tools
# --------------------------------------------------------------------------------------------------
FROM ubuntu:16.04
MAINTAINER Rafael Catrou <rafael@localhost>

RUN \
    apt-get update -y && \
    apt-get upgrade -y

RUN \
    apt-get install -y make && \
    apt-get install -y sudo && \    
    apt-get install -y expect && \
    apt-get install -y curl && \
    apt-get install -y wget && \
    apt-get install -y unzip

RUN \
    apt-get install -y apt-utils && \
    apt-get install -y texinfo

# --------------------------------------------------------------------------------------------------
# Python 2.x (base)
# --------------------------------------------------------------------------------------------------
RUN \
    apt-get install -y python2.7 && \
    apt-get install -y python-pip && \
    pip install --upgrade pip

# --------------------------------------------------------------------------------------------------
# Install Zlib
# --------------------------------------------------------------------------------------------------
RUN apt-get install -y zlib1g-dev

# --------------------------------------------------------------------------------------------------
# Install GNAT 2016
# --------------------------------------------------------------------------------------------------
# Get setup
RUN mkdir -p /root/tools/gnat
WORKDIR /root/tools/gnat
RUN \
    wget http://mirrors.cdn.adacore.com/art/5739cefdc7a447658e0b016b && \
    mv 5739cefdc7a447658e0b016b gnat-gpl-2016-x86_64-linux-bin.tar.gz && \
    sync

RUN tar -zxvf gnat-gpl-2016-x86_64-linux-bin.tar.gz
RUN \rm gnat-gpl-2016-x86_64-linux-bin.tar.gz

COPY src/gnat_install.expect /root/tools/gnat/gnat-gpl-2016-x86_64-linux-bin
# Install
WORKDIR /root/tools/gnat/gnat-gpl-2016-x86_64-linux-bin
RUN \
    chmod +x /root/tools/gnat/gnat-gpl-2016-x86_64-linux-bin/gnat_install.expect && \
    sync
RUN expect gnat_install.expect
ENV PATH /usr/gnat/bin:$PATH
# Valid that installation is fine
RUN which gnat


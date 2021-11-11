# Copyright 2018 Royal Bank of Scotland

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Base image from (http://phusion.github.io/baseimage-docker)
FROM phusion/baseimage:0.9.22

# Set up Version
ENV version=3.0.0

# Working directory for Corda
WORKDIR /opt/corda
ENV HOME=/opt/corda

# Set image labels
LABEL net.corda.version=${version}
LABEL vendor="R3"
MAINTAINER <devops@r3.com>

# Install OpenJDK from zulu.org and update system
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0x219BD9C9 \
 && (echo "deb http://repos.azulsystems.com/ubuntu stable main" >> /etc/apt/sources.list.d/zulu.list) \
 && apt-get -qq update \
 && apt-get -y upgrade -y -o Dpkg::Options::="--force-confold" \
 && apt-get -qqy install zulu-8 ntp \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add user corda
RUN groupadd corda \
 && useradd -c "Corda user" -g corda -m -s /bin/bash corda

# Create /opt/corda directory
RUN mkdir -p /opt/corda/logs && mkdir -p /opt/service/corda

# Copy corda jar
ADD http://central.maven.org/maven2/net/corda/corda/corda-3.0/corda-corda-3.0.jar /opt/corda/corda.jar

# Fix permissions for Openshift security contexts
RUN chgrp -R 0 /opt/corda \
 && chmod -R g=u /opt/corda \
 && chown -R corda:corda /opt/corda

USER corda

# Start runit
ENTRYPOINT [ "java", "-jar", "corda.jar" ]
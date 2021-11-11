# Copyright 2016 Bryan J. Hong
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM ubuntu:xenial

MAINTAINER bryan@turbojets.net

ENV DEBIAN_FRONTEND noninteractive
ENV DIST=ubuntu
ENV RELEASE=xenial

# Update APT repository and install packages
RUN apt-get -qq update                  \
 && apt-get -y -qq install aptly           \
                       bzip2           \
                       gnupg           \
                       gpgv            \
                       graphviz        \
                       supervisor      \
                       nginx           \
                       wget            \
                       xz-utils        \
                       apt-utils      \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Install Aptly Configuration
COPY assets/aptly.conf /etc/aptly.conf

# Install Nginx Config
COPY assets/nginx.conf.sh /opt/nginx.conf.sh
RUN rm /etc/nginx/sites-enabled/*
COPY assets/supervisord.nginx.conf /etc/supervisor/conf.d/nginx.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Install scripts
COPY assets/*.sh /opt/
COPY assets/update_mirror/update_mirror_ubuntu.sh /opt/update_mirror.sh

# Bind mount location
VOLUME [ "/opt/aptly" ]

# Execute Startup script when container starts
ENTRYPOINT [ "/opt/startup.sh" ]

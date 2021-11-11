# Copyright (C) 2017 AOSP/QEMU/SPICE build environment in docker
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#******************************************************************************
#
# Dockerfile - build environment for AOSP/QEMU/SPICE
#              This docker image can be used to build Android 6, QEMU and SPICE
#
# Copyright (c) 2017 Roger Ye.  All rights reserved.
#
#******************************************************************************
#

FROM shugaoye/docker-aosp:ubuntu14.04-JDK7

MAINTAINER Roger Ye <shugaoye@yahoo.com>

RUN apt-get update
RUN apt-get build-dep -y qemu spice-gtk
RUN apt-get install -y openssh-server net-tools gettext vim-common vim-tiny python-pip libxml2-dev \
	libtext-csv-perl gtk-doc-tools libpixman-1-dev libjpeg-dev valac libssl-dev \
	libgbm-dev libsdl2-dev libgtk-3-dev libgles2-mesa-dev libepoxy-dev python-mako libglib2.0-dev

RUN mkdir /var/run/sshd
RUN export LC_ALL=C

RUN pip install pyomo -U
RUN echo 'root:root' | chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]

# The persistent data will be in these two directories, everything else is
# considered to be ephemeral
VOLUME ["/tmp/ccache", "/home/aosp"]

# Improve rebuild performance by enabling compiler cache
ENV USE_CCACHE 1
ENV CCACHE_DIR /tmp/ccache

# Work in the build directory, repo is expected to be init'd here
WORKDIR /home/aosp

COPY utils/bash.bashrc /root/bash.bashrc
RUN chmod 755 /root /root/bash.bashrc
COPY utils/setup_build.sh /root/setup_build.sh
RUN chmod 755 /root/setup_build.sh
COPY utils/docker_entrypoint.sh /root/docker_entrypoint.sh
ENTRYPOINT ["/root/docker_entrypoint.sh"]

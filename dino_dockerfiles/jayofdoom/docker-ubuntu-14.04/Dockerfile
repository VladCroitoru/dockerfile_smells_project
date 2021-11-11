#Copyright 2013 Rackspace, Inc.
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

# Builds a 14.04 (alpha) from the latest saucy image.
FROM stackbrew/ubuntu:13.10
MAINTAINER jay.faulkner@rackspace.com
ENV DEBIAN_FRONTEND noninteractive

# Work around initramfs-tools running on kernel 'upgrade': <http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>
ENV INITRD No

# Work around initscripts trying to mess with /dev/shm: <https://bugs.launchpad.net/launchpad/+bug/974584>
# Used by our `src/ischroot` binary to behave in our custom way, to always say we are in a chroot.
ENV FAKE_CHROOT 1
RUN mv /usr/bin/ischroot /usr/bin/ischroot.original
ADD src/ischroot /usr/bin/ischroot

# Configure no init scripts to run on package updates.
ADD src/policy-rc.d /usr/sbin/policy-rc.d

RUN sed -i 's/saucy/trusty/g' /etc/apt/sources.list
RUN echo 'force-unsafe-io' | tee /etc/dpkg/dpkg.cfg.d/02apt-speedup
RUN echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb || true";};' | tee /etc/apt/apt.conf.d/no-cache
RUN echo 'Acquire::http {No-Cache=True;};' | tee /etc/apt/apt.conf.d/no-http-cache

RUN apt-get update -y && apt-get dist-upgrade -y

RUN apt-get clean

RUN rm -rf /var/cache/apt/* 

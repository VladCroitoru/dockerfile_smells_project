FROM ubuntu:trusty
MAINTAINER Nimbix, Inc.

# DEPRECATED:  Please use https://github.com/nimbix/image-common to set up
#   your app images for JARVICE.

# upstart fixes
# init-fake.conf from https://raw.githubusercontent.com/tianon/dockerfiles/master/sbin-init/ubuntu/upstart/14.04/init-fake.conf
ADD init-fake.conf /etc/init/fake-container-events.conf
RUN rm /usr/sbin/policy-rc.d; \
	rm /sbin/initctl; dpkg-divert --rename --remove /sbin/initctl
RUN echo '# /lib/init/fstab: cleared out for bare-bones Docker' >/lib/init/fstab

# base OS
ENV DEBIAN_FRONTEND noninteractive
ADD https://github.com/nimbix/image-common/archive/master.zip /tmp/nimbix.zip
WORKDIR /tmp
RUN apt-get update && apt-get -y install zip unzip && unzip nimbix.zip && rm -f nimbix.zip
RUN /tmp/image-common-master/setup-nimbix.sh
RUN touch /etc/init.d/systemd-logind && apt-get update && apt-get -y install xz-utils openssh-server libpam-systemd libmlx4-1 libmlx5-1 iptables infiniband-diags && apt-get clean && locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8

# Nimbix JARVICE emulation
EXPOSE 22
RUN mkdir -p /usr/lib/JARVICE && cp -a /tmp/image-common-master/tools /usr/lib/JARVICE
RUN ln -s /usr/lib/JARVICE/tools/noVNC/images/favicon.png /usr/lib/JARVICE/tools/noVNC/favicon.png && ln -s /usr/lib/JARVICE/tools/noVNC/images/favicon.png /usr/lib/JARVICE/tools/noVNC/favicon.ico
WORKDIR /usr/lib/JARVICE/tools/noVNC/utils
RUN ln -s websockify /usr/lib/JARVICE/tools/noVNC/utils/websockify.py && ln -s websockify /usr/lib/JARVICE/tools/noVNC/utils/wsproxy.py
WORKDIR /tmp
RUN cp -a /tmp/image-common-master/etc /etc/JARVICE && chmod 755 /etc/JARVICE && rm -rf /tmp/image-common-master
RUN mkdir -m 0755 /data && chown nimbix:nimbix /data

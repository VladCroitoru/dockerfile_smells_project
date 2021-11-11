FROM centos:6
MAINTAINER Nimbix, Inc.

# base OS
RUN yum -y update
ADD https://github.com/nimbix/image-common/archive/master.zip /tmp/nimbix.zip
WORKDIR /tmp
RUN yum -y install zip unzip xz tar file sudo openssh-server infiniband-diags openmpi perftest libibverbs-utils libmthca libcxgb4 libmlx4 libmlx5 dapl compat-dapl dap.i686 compat-dapl.i686 && yum clean all && unzip nimbix.zip && rm -f nimbix.zip
RUN /tmp/image-common-master/setup-nimbix.sh
RUN rm -f /etc/sysconfig/network-scripts/ifcfg-eth0 && echo '/dev/root / rootfs defaults 0 0' >/etc/fstab
RUN sed -i 's|.sbin.start_udev||' /etc/rc.sysinit
RUN sed -i 's|.sbin.start_udev||' /etc/rc.d/rc.sysinit
RUN chkconfig udev-post off

# Nimbix JARVICE emulation
EXPOSE 22
RUN mkdir -p /usr/lib/JARVICE && cp -a /tmp/image-common-master/tools /usr/lib/JARVICE
RUN ln -s /usr/lib/JARVICE/tools/noVNC/images/favicon.png /usr/lib/JARVICE/tools/noVNC/favicon.png && ln -s /usr/lib/JARVICE/tools/noVNC/images/favicon.png /usr/lib/JARVICE/tools/noVNC/favicon.ico
WORKDIR /usr/lib/JARVICE/tools/noVNC/utils
RUN ln -s websockify /usr/lib/JARVICE/tools/noVNC/utils/websockify.py && ln -s websockify /usr/lib/JARVICE/tools/noVNC/utils/wsproxy.py
WORKDIR /tmp
RUN cp -a /tmp/image-common-master/etc /etc/JARVICE && chmod 755 /etc/JARVICE && rm -rf /tmp/image-common-master && mkdir -m 0755 /data && chown nimbix:nimbix /data
ADD hosts /etc/hosts

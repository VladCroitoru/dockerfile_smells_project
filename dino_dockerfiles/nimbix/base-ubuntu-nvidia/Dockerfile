FROM nvidia/cuda:8.0-cudnn5-devel
MAINTAINER Nimbix, Inc. <support@nimbix.net>

# base OS
ENV DEBIAN_FRONTEND noninteractive
ADD https://github.com/nimbix/image-common/archive/master.zip /tmp/nimbix.zip
WORKDIR /tmp
RUN apt-get update && apt-get -y install sudo zip unzip && unzip nimbix.zip && rm -f nimbix.zip
RUN /tmp/image-common-master/setup-nimbix.sh
RUN touch /etc/init.d/systemd-logind && apt-get -y install module-init-tools xz-utils vim openssh-server libpam-systemd libmlx4-1 libmlx5-1 iptables infiniband-diags build-essential curl libibverbs-dev libibverbs1 librdmacm1 librdmacm-dev rdmacm-utils libibmad-dev libibmad5 byacc flex git cmake screen grep && apt-get clean && locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8

# Nimbix JARVICE emulation
EXPOSE 22
RUN mkdir -p /usr/lib/JARVICE && cp -a /tmp/image-common-master/tools /usr/lib/JARVICE
RUN cp -a /tmp/image-common-master/etc /etc/JARVICE && chmod 755 /etc/JARVICE && rm -rf /tmp/image-common-master
RUN mkdir -m 0755 /data && chown nimbix:nimbix /data
RUN sed -ie 's/start on.*/start on filesystem/' /etc/init/ssh.conf


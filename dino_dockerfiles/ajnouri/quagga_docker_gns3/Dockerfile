# Use phusion/baseimage as base image. To make your builds
# reproducible, make sure you lock down to a specific version, not
# to `latest`! See
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md
# for a list of version numbers.
FROM phusion/baseimage:0.9.16

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Tell debconf to run in non-interactive mode
ENV DEBIAN_FRONTEND noninteractive


# Update the source list for appropriate repository, trusty 14.04 LTS, in this case.
# Generated from:
# https://wiki.ubuntu.com/DevelopmentCodeNames
# http://repogen.simplylinux.ch/

RUN echo "deb http://fr.archive.ubuntu.com/ubuntu/ trusty main" >> /etc/apt/sources.list
RUN echo "deb-src http://fr.archive.ubuntu.com/ubuntu/ trusty main universe" >> /etc/apt/sources.list
RUN echo "deb http://fr.archive.ubuntu.com/ubuntu/ trusty-security main" >> /etc/apt/sources.list
RUN echo "deb http://fr.archive.ubuntu.com/ubuntu/ trusty-updates main" >> /etc/apt/sources.list
RUN echo "deb-src http://fr.archive.ubuntu.com/ubuntu/ trusty-security main universe" >> /etc/apt/sources.list
RUN echo "deb-src http://fr.archive.ubuntu.com/ubuntu/ trusty-updates main universe" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y quagga iperf inetutils-traceroute iputils-tracepath mtr dnsutils tcpdump packeth

RUN rm -f /etc/service/sshd/down
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh
RUN mkdir -p /root/.ssh

# Permanently enable the insecure-key
RUN /usr/sbin/enable_insecure_key

RUN echo 'root:gns3quagga' | chpasswd
RUN sed -i "s/#PermitRootLogin without-password/PermitRootLogin yes/" /etc/ssh/sshd_config
ADD quagga.sh /sbin/quagga.sh

#RUN sysctl -w net.ipv4.conf.all.forwarding=1
#RUN sysctl -w net.ipv4.conf.default.forwarding=1
#RUN sysctl -w net.ipv4.ip_forward=1
#RUN sysctl -w net.ipv6.conf.all.forwarding=1
#RUN sysctl -w net.ipv6.conf.default.forwarding=1

RUN touch /etc/quagga/babeld.conf && \
	touch /etc/quagga/bgpd.conf && \
	touch /etc/quagga/isisd.conf && \
	touch /etc/quagga/ospf6d.conf && \
	touch /etc/quagga/ospfd.conf && \
	touch /etc/quagga/ripd.conf && \
	touch /etc/quagga/ripngd.conf && \
	touch /etc/quagga/vtysh.conf && \
	touch /etc/quagga/zebra.conf 

# Fix <END> screen with vtysh
RUN echo "export VTYSH_PAGER=more" >>  /etc/bash.bashrc
RUN echo "VTYSH_PAGER=more" >> /etc/environment

RUN sed -i 's/no/yes/g' /etc/quagga/daemons 
RUN chown -R quagga /etc/quagga

#CMD ["/etc/init.d/quagga"]

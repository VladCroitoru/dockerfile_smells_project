FROM debian:wheezy
MAINTAINER Emre Bastuz <info@hml.io>

# Environment
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

# Get current
RUN apt-get update -y
RUN apt-get dist-upgrade -y

# Install packages 
RUN apt-get install -y wget bind9

# Install vulnerable bind version from wayback/snapshot archive
RUN \
wget http://snapshot.debian.org/archive/debian-security/20150707T195014Z/pool/updates/main/b/bind9/libbind9-80_9.8.4.dfsg.P1-6%2Bnmu2%2Bdeb7u5_amd64.deb \
 -O /tmp/libbind9-80_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
wget http://snapshot.debian.org/archive/debian-security/20150707T195014Z/pool/updates/main/b/bind9/libdns88_9.8.4.dfsg.P1-6%2Bnmu2%2Bdeb7u5_amd64.deb \
 -O /tmp/libdns88_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
wget http://snapshot.debian.org/archive/debian-security/20150707T195014Z/pool/updates/main/b/bind9/libisc84_9.8.4.dfsg.P1-6%2Bnmu2%2Bdeb7u5_amd64.deb \
 -O /tmp/libisc84_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
wget http://snapshot.debian.org/archive/debian-security/20150707T195014Z/pool/updates/main/b/bind9/libisccc80_9.8.4.dfsg.P1-6%2Bnmu2%2Bdeb7u5_amd64.deb \
 -O /tmp/libisccc80_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
wget http://snapshot.debian.org/archive/debian-security/20150707T195014Z/pool/updates/main/b/bind9/libisccfg82_9.8.4.dfsg.P1-6%2Bnmu2%2Bdeb7u5_amd64.deb \
 -O /tmp/libisccfg82_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
wget http://snapshot.debian.org/archive/debian-security/20150707T195014Z/pool/updates/main/b/bind9/liblwres80_9.8.4.dfsg.P1-6%2Bnmu2%2Bdeb7u5_amd64.deb \
 -O /tmp/liblwres80_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
wget http://snapshot.debian.org/archive/debian-security/20150707T195014Z/pool/updates/main/b/bind9/bind9utils_9.8.4.dfsg.P1-6%2Bnmu2%2Bdeb7u5_amd64.deb \
 -O /tmp/bind9utils_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
wget http://snapshot.debian.org/archive/debian-security/20150707T195014Z/pool/updates/main/b/bind9/bind9_9.8.4.dfsg.P1-6%2Bnmu2%2Bdeb7u5_amd64.deb \
 -O /tmp/bind9_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
dpkg -i /tmp/libbind9-80_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
dpkg -i /tmp/libdns88_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
dpkg -i /tmp/libisc84_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
dpkg -i /tmp/libisccc80_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
dpkg -i /tmp/libisccfg82_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
dpkg -i /tmp/liblwres80_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
dpkg -i /tmp/bind9utils_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb && \
dpkg -i /tmp/bind9_9.8.4.dfsg.P1-6+nmu2+deb7u5_amd64.deb

ENV DEBIAN_FRONTEND noninteractive

# Edit the defaults file to start bind in foreground
RUN sed -i 's/^OPTIONS="-u bind"/OPTIONS="-u bind -g -d1"/g' /etc/default/bind9

# Clean up 
RUN apt-get autoremove
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Expose the port for usage with the docker -P switch
EXPOSE 53/udp

# Run the process
CMD ["/etc/init.d/bind9", "start"]

#
# Dockerfile for vulnerability as a service - CVE-2015-5477
# Vulnerable version of bind9 to showcase DDoS condition
#

FROM centos:centos6
MAINTAINER moremagic <itoumagic@gmail.com>

# Install wget etc...
RUN yum install -y wget passwd openssh-server initscripts \
    && wget http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm \
    && rpm -ivh rpmforge-release-*.rpm \
    && yum -y update

# ssh
RUN ssh-keygen -h -t rsa -f /etc/ssh/ssh_host_rsa_key \
    && ssh-keygen -h -t dsa -f /etc/ssh/ssh_host_dsa_key \
    && echo "root" | passwd --stdin root

# dante install
RUN yum -y install dante* \
    && printf '\
logoutput: syslog stdout /var/log/sockd.log \n\
debug: 2 \n\
 \n\
internal: eth0 port = 1080 \n\
external: eth0 \n\
socksmethod: username none \n\
clientmethod: none \n\
user.privileged: nobody \n\
user.unprivileged: nobody \n\
client pass { \n\
    from: 0.0.0.0/0 port 1-65535 to: 0.0.0.0/0 \n\
} \n\
socks pass { \n\
    from: 0.0.0.0/0 to: 0.0.0.0/0 \n\
    protocol: tcp udp \n\
} \n\
' >> /etc/sockd.conf \
    && printf '\
route { \n\
    from: 0.0.0.0/0 to: 0.0.0.0/0 via: direct \n\
    proxyprotocol: socks_v5 \n\
} \n\
' >> /etc/socks.conf


RUN printf '\
\#!/bin/bash \n\
/etc/init.d/network restart \n\
/etc/init.d/sockd start \n\
/usr/sbin/sshd -D \n\
while true \n\
do \n\
    sleep 10 \n\
done \n\
' >> /etc/service.sh \
    && chmod +x /etc/service.sh

EXPOSE 22 1080
CMD /etc/service.sh

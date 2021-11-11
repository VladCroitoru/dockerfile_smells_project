FROM centos:latest

MAINTAINER zzzshanghai

##########################################################################
# all yum updates here
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-*
RUN yum update -y

##########################################################################
# all yum installations here
RUN yum install -y sudo passwd openssh-server openssh-clients wget tar screen vixie-cron crontabs strace telnet perl libpcap bc patch ntp dnsmasq

##########################################################################
# start sshd to generate host keys, patch sshd_config and enable yum repos
RUN (ssh-keygen -q -b 2048 -N '' -t rsa -f /etc/ssh/ssh_host_rsa_key; \
     ssh-keygen -q -b 1024 -N '' -t dsa -f /etc/ssh/ssh_host_dsa_key; \
     ssh-keygen -q -N '' -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key; \
     ssh-keygen -q -N '' -t ed25519 -f /etc/ssh/ssh_host_ed25519_key)

RUN (sed -i 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config; \
     sed -i 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config; \
     sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config; \
     sed -i 's/enabled=0/enabled=1/' /etc/yum.repos.d/CentOS-Base.repo)

RUN (mkdir -p /root/.ssh/; \
     echo "StrictHostKeyChecking=no" > /root/.ssh/config; \
     echo "UserKnownHostsFile=/dev/null" >> /root/.ssh/config)


##########################################################################
# passwords 
RUN echo "root:password" | chpasswd

EXPOSE 80
EXPOSE 22

CMD /usr/sbin/crond; /usr/sbin/sshd -D

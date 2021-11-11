FROM centos:5

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
RUN (service sshd start; \
     sed -i 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config; \
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

CMD service crond start; /usr/sbin/sshd -D

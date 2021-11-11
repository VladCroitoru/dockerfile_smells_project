FROM fedora:heisenbug
MAINTAINER "Mike Taylor" <mike@whatsmycut.com>
ENV container docker
RUN yum -y update; yum clean all;
RUN yum -y install systemd; yum clean all; 
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*; \
rm -f /etc/systemd/system/*.wants/*; \
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*; \
rm -f /lib/systemd/system/anaconda.target.wants/*; 

RUN yum -y update && yum install -y sh wget sudo bind bind-utils epel-release initscripts; \
yum clean all;

## INSTALL JAVA 8u151-b12
# Prepare environment 
ENV JAVA_HOME /opt/java

# Install Oracle Java8
ENV JAVA_VERSION 8u151
ENV JAVA_BUILD 8u151-b12
ENV JAVA_DL_HASH e758a0de34e24606bca991d704f6dcbf

RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" \
 http://download.oracle.com/otn-pub/java/jdk/${JAVA_BUILD}/${JAVA_DL_HASH}/jre-${JAVA_VERSION}-linux-x64.rpm && \
 yum localinstall -y jre-${JAVA_VERSION}-linux-x64.rpm \
 rm jre*.rpm \
 mv jre* ${JAVA_HOME} 

VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]
ENTRYPOINT [ "/bin/sh", "-c", "java -version" ]


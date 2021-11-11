# Install centos 7

FROM centos
MAINTAINER Lichia Lu <lichialu@gmail.com>
ENV container docker
RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs
RUN yum install -y wget tar zip
RUN yum -y update; yum clean all; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;
VOLUME [ "/sys/fs/cgroup" ]

# Install Oracle JDK 8
RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u45-b14/jdk-8u45-linux-x64.rpm && rpm -ivh jdk-8u45-linux-x64.rpm && rm -rf jdk-8u45-linux-x64.rpm
# Set the JAVA_HOME variable
ENV JAVA_HOME /usr/java/jdk1.8.0_45

CMD ["/usr/sbin/init"]

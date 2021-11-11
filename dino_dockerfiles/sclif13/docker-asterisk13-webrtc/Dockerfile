FROM centos:centos7
MAINTAINER Alexandr Opryshko "sclif13@gmail.com" 
RUN yum -y clean all && yum -y update && yum -y install epel-release && yum -y install wget vim tar htop gcc-c++ make gnutls-devel kernel-devel libxml2-devel ncurses-devel subversion doxygen texinfo curl-devel net-snmp-devel neon-devel uuid-devel libuuid-devel sqlite-devel sqlite git speex-devel gsm-devel libtool && ldconfig

WORKDIR /usr/src
RUN wget http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-13.14.0.tar.gz && tar -zxvf asterisk-13.14.0.tar.gz

WORKDIR /usr/src/asterisk-13.14.0/contrib/scripts
RUN ./install_prereq install && ./install_prereq install-unpackaged && ./get_mp3_source.sh

WORKDIR /usr/src/asterisk-13.14.0
RUN ./configure CFLAGS='-g -O2' --libdir=/usr/lib64 && make && make install && make samples && yum -y clean all

WORKDIR /root
CMD ["/usr/sbin/asterisk", "-vvvvvvv"]

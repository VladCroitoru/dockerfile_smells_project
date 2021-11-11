FROM fedora

ADD ./seagull-1.8.2-Linux_RHEL6U1_X86_64.tar.gz /tmp

RUN yum install -y ksh libstdc++ && \
 cd /tmp/packages/ && \
 rpm -Uvh seagull-core-1.8.2-linux-2.6-intel.rpm \
   seagull-diameter-protocol-1.8.2-linux-2.6-intel.rpm \
   seagull-radius-protocol-1.8.2-linux-2.6-intel.rpm

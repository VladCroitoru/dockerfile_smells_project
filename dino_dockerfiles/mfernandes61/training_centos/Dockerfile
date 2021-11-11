FROM consol/centos-xfce-vnc
MAINTAINER Mark Fernandes <mark.fernandes@quadram.ac.uk>

USER root
RUN yum -y install man
# Putting the man pages back in 
RUN sed -i '/tsflags=nodocs/d' /etc/yum.conf
RUN yum -y update & yum -y reinstall man-pages man- man less

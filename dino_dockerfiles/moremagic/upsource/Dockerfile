FROM centos
MAINTAINER moremagic <itoumagic@gmail.com>

# Install wget etc...
RUN yum install -y passwd openssh-server openssh-clients initscripts
RUN yum install -y install java-1.8.0-* git wget curl tar zip unzip \
    && yum -y update

# ssh
RUN echo 'root:root' | chpasswd
RUN /usr/sbin/sshd-keygen

# upsource
RUN wget https://download.jetbrains.com/upsource/upsource-2.5.5047.zip \
    && unzip upsource-2.5.5047.zip 
RUN printf '* - memlock unlimited \n\ 
* - nofile 100000 \n\ 
* - nproc 32768 \n\ 
* - as unlimited \n\ 
' >> /etc/security/limits.conf

RUN printf '#!/bin/bash \n\
export JAVA_HOME=/usr/lib/jvm/java-openjdk/ \n\
/bin/sh /Upsource/bin/upsource.sh start \n\
/usr/sbin/sshd -D \n\
tail -f /var/null  \n\
' >> /etc/service.sh \
    && chmod +x /etc/service.sh

EXPOSE 22 8080 
CMD /etc/service.sh

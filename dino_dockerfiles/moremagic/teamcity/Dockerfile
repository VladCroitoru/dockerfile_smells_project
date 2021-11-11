FROM centos
MAINTAINER moremagic <itoumagic@gmail.com>

# Install wget etc...
RUN yum install -y passwd openssh-server openssh-clients initscripts
RUN yum install -y install java-1.8.0-* git wget curl tar zip \
    && yum -y update

# ssh
RUN echo 'root:root' | chpasswd
RUN /usr/sbin/sshd-keygen

# set locale
RUN yum -y reinstall glibc-common
RUN localedef -v -c -i ja_JP -f UTF-8 ja_JP.UTF-8; echo "";

env LANG=ja_JP.UTF-8
RUN rm -f /etc/localtime
RUN ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# teamcity
RUN wget https://download.jetbrains.com/teamcity/TeamCity-10.0.tar.gz \
    && tar zxvf TeamCity-10.0.tar.gz

ENV JAVA_HOME /usr/lib/jvm/java-1.8.0

RUN printf '#!/bin/bash \n\
mkdir -p /TeamCity/buildAgent/logs/ \n\
/TeamCity/bin/runAll.sh start \n\
/usr/sbin/sshd -D \n\
tail -f /var/null  \n\
' >> /etc/service.sh \
    && chmod +x /etc/service.sh

EXPOSE 22 8111
CMD /etc/service.sh

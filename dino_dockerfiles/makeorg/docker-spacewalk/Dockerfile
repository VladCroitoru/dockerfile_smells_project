#
# Dockerfile - Spacewalk
#
# inspired by https://hub.docker.com/r/bashell/spacewalk/
# same without privileged and with spacewalk 2.7
# 
# - Run
# docker run --cap-add=SYS_PTRACE -d --name="spacewalk" -p 80:80 -p 443:443 makeorg/docker-spacewalk

# 1. Base images
FROM     centos:6
MAINTAINER Vincent Baret <vb@make.org>

# 2. Set the environment variable
WORKDIR /opt
ENV VERSION=1.0
ENV RELEASE=0

# 3. Add the epel, spacewalk, jpackage, supervisord
#ADD conf/jpackage.repo /etc/yum.repos.d/jpackage.repo
RUN yum install -y epel-release \
 && rpm -Uvh http://yum.spacewalkproject.org/2.7/RHEL/6/x86_64/spacewalk-repo-2.7-2.el6.noarch.rpm \
 && yum repolist && yum update -y && yum upgrade -y \
 && cd /etc/yum.repos.d && curl -O https://copr.fedorainfracloud.org/coprs/g/spacewalkproject/java-packages/repo/epel-7/group_spacewalkproject-java-packages-epel-7.repo \
 && curl -O https://copr.fedorainfracloud.org/coprs/g/spacewalkproject/epel6-addons/repo/epel-6/group_spacewalkproject-epel6-addons-epel-6.repo \
 && yum install -y spacewalk-setup-postgresql spacewalk-postgresql tomcat-native python-setuptools \
 && yum clean all \
 && easy_install -i https://pypi.python.org/pypi pip && pip install supervisor && pip install --upgrade meld3==0.6.10 && mkdir /etc/supervisord.d \
 && rm -rf /root/.cache

# 4. Install supervisord config
ADD conf/supervisord.conf /etc/supervisord.d/supervisord.conf

# 5. Install spacewalk initial and running scripts
ADD conf/answer.txt   /opt/answer.txt
ADD conf/spacewalk.sh /opt/spacewalk.sh
ADD conf/postgresql /etc/init.d/postgresql

# 6. Start supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.d/supervisord.conf"]

# System Log
VOLUME /var/log

# PostgreSQL Data
VOLUME /var/lib/pgsql/data

# RPM repository
VOLUME /var/satellite

# Bootstrap directory
VOLUME /var/www/html/pub

# Port
EXPOSE 80 443

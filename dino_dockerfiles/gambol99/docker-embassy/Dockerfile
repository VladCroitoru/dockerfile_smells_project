#
#   Author: Rohith (gambol99@gmail.com)
#   Date: 2015-01-16 16:53:23 +0000 (Fri, 16 Jan 2015)
#
#  vim:ts=2:sw=2:et
#

# Embassy Service is a base container with the embassy service proxy embedded
FROM centos:centos7
MAINTAINER Rohith <gambol99@gmail.com>

ADD config/embassy.ini /etc/supervisord.d/embassy.ini
ADD config/embassy.init /bin/embassy.init
ADD config/runner.sh /bin/runner.sh

# step: we need the epel repository
RUN yum install -y http://www.mirrorservice.org/sites/dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm

# step: lets install embassy
RUN curl -ksL https://drone.io/github.com/gambol99/embassy/files/embassy.gz > /bin/embassy.gz && \
    md5sum /bin/embassy.gz && \
    gunzip /bin/embassy.gz && \
    chmod +x /bin/embassy && \
    chmod +x /bin/embassy.init && \
    chmod +x /bin/runner.sh

# step: lets install supervisord
RUN yum install -y supervisor

ENTRYPOINT [ "/bin/runner.sh" ]

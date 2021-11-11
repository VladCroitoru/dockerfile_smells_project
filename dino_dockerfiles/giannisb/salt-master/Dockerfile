FROM centos:centos7

MAINTAINER Giannis Betas

RUN yum -y update && \
curl -O https://repo.saltstack.com/yum/redhat/latest/x86_64/2016.11/SALTSTACK-GPG-KEY.pub && \
rpm --import SALTSTACK-GPG-KEY.pub && \
yum -y install https://repo.saltstack.com/yum/redhat/salt-repo-latest-2.el7.noarch.rpm && \
# yum clean all
#
# RUN yum clean expire-cache && \
yum -y update && \
yum -y install salt-master && \
yum clean all

RUN useradd -r -s /bin/false salt -d  /var/cache/salt && \
mkdir /var/run/salt && \
chown -R salt /etc/salt /var/cache/salt /var/log/salt /var/run/salt

EXPOSE 4505 4506

ENTRYPOINT [ "salt-master" ]

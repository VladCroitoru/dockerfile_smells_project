FROM centos:7
MAINTAINER Stefan Monko, PosAm s.r.o.

# Arguments
ARG envToCreate=container

# Update OS
RUN yum update -y

# Install salt
RUN yum -y install https://repo.saltstack.com/yum/redhat/salt-repo-latest-2.el7.noarch.rpm && \
 yum install -y salt-master && \
 yum install -y salt-syndic && \
 sed -i -e "/hash_type:/c\hash_type: sha256" /etc/salt/master && \
 yum clean all

RUN yum install -y salt-minion

ADD run_syndic.sh /root/run_syndic.sh
RUN chmod a+x /root/run_syndic.sh


CMD ["/root/run_syndic.sh"]

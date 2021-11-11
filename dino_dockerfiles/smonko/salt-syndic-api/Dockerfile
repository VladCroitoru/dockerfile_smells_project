FROM centos:7
MAINTAINER Stefan Monko, PosAm s.r.o.

# Arguments
ARG envToCreate=container

RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && yum update -y && \
 yum -y install https://repo.saltstack.com/yum/redhat/salt-repo-latest-2.el7.noarch.rpm && \
 yum install -y salt-master && \
 yum install -y salt-syndic && \
 sed -i -e "/hash_type:/c\hash_type: sha256" /etc/salt/master && \
 yum install -y salt-minion && \
 yum install -y salt-api && \
 yum install -y git && \
 yum install -y python-cherrypy && \
 yum install -y pyOpenSSL && \
 yum install -y python-ldap && \
 yum install -y python-pip python-wheel && \
 salt-call --local tls.create_self_signed_cert && \
 useradd saltapi && \
 echo "saltapi" | passwd --stdin "saltapi" && \
 pip install --upgrade pip && pip install gitpython &&\
 yum clean all

ADD run_syndic.sh /root/run_syndic.sh
RUN chmod a+x /root/run_syndic.sh


CMD ["/root/run_syndic.sh"]

FROM centos

RUN yum install -y -q epel-release && yum -y -q update && yum -y -q install ansible \
yum -y -q install openssh-server openssh-clients
VOLUME /home/ansible
ENTRYPOINT /bin/bash

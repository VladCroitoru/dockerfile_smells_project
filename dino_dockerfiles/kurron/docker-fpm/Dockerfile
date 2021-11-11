FROM centos:7

MAINTAINER Ron Kurr <kurr@kurron.org>
 
ADD install-ansible-centos.sh /root
RUN /root/install-ansible-centos.sh
ADD ansible /root/ansible
WORKDIR /root/ansible
RUN ansible-playbook playbook.yml --connection local

VOLUME ["/pwd"]
WORKDIR /pwd

ENTRYPOINT ["fpm"]
CMD ["--version"]

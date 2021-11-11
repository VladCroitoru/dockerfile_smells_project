FROM ubuntu:14.04
MAINTAINER Bobby Outlaw  <law.zero@gmail.com>
RUN apt-get -y update && \
    apt-get install -y python-yaml python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools \
    python-pkg-resources git nano python-pip ssh openssh-server 
RUN apt-key adv \
    --keyserver keyserver.ubuntu.com \
    --recv 6125E2A8C77F2818FB7BD15B93C4A3FD7BB9C367
RUN mkdir /etc/ansible/
RUN mkdir /opt/ansible/
RUN echo '[local]\nlocalhost          ansible_connection=local\n' > /etc/ansible/hosts
RUN echo '[defaults]\nhostfile = /etc/ansible/hosts\nhost_key_checking=False\ntimeout = 5\n' > /opt/ansible/ansible.cfg
RUN git clone http://github.com/ansible/ansible.git /opt/ansible/ansible
WORKDIR /opt/ansible/ansible
RUN git submodule update --init
ENV PATH /opt/ansible/ansible/bin:/bin:/usr/bin:/sbin:/usr/sbin
ENV PYTHONPATH /opt/ansible/ansible/lib
ENV ANSIBLE_LIBRARY /opt/ansible/ansible/library

    
    

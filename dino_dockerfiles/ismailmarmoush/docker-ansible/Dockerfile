FROM debian:latest

MAINTAINER Ismail Marmoush<marmoushismail@gmail.com>

### Install Utils
RUN apt-get update && apt-get install -y git curl apt-utils gcc make build-essential libssl-dev libffi-dev man nano

RUN apt-get update && apt-get install -y python2.7 python2.7-dev python-dev
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python2.7 get-pip.py
RUN pip install --upgrade pip
RUN pip install PyYaml paramiko Jinja2 httplib2 six netaddr


### Install Ansible
ARG ANSIBLE_DIR=/ansible

RUN mkdir -p $ANSIBLE_DIR
RUN git clone git://github.com/ansible/ansible.git --recursive $ANSIBLE_DIR

RUN mkdir -p /etc/ansible
RUN echo 'localhost' > /etc/ansible/hosts

ENV ENV_SETUP ${ANSIBLE_DIR}/hacking/env-setup

RUN echo "source ${ENV_SETUP} -q" >> /etc/bash.bashrc

ENV CODE echo defaultBehaviour
CMD ["/bin/bash","-c","chmod +x ${ENV_SETUP} && source ${ENV_SETUP} -q && ${CODE}"]

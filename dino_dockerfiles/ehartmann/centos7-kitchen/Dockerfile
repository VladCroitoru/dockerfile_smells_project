# Defines Docker image suitable for testing cookbooks on CentOS 7.
#
# This handles a number of idiosyncrasies with systemd so it can be 
# run as the root process of the container, making it behave like a 
# normal VM but without the overhead. 
FROM centos:centos7

MAINTAINER Eric Hartmann <hartmann.eric@gmail.com>

ENV ANSIBLE_VERSION 2.0.1.0

# skip installing gem documentation
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"

# Setup container to run Systemd as root process, start an SSH 
# daemon, and provision a user for test-kitchen to connect as.
RUN yum clean all && \ 
    yum -y install epel-release && \
# Dependencies for Ansible    
    yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools git python-pip \
                   crontabs curl initscripts net-tools passwd sudo tar which

# Remove the requirements of tty for sudo
RUN sed -i "s/^.*requiretty/#Defaults requiretty/" /etc/sudoers


# Install Ansible    
RUN  mkdir /etc/ansible/ && \
    echo -e '[local]\nlocalhost' > /etc/ansible/hosts && \
    pip install ansible==${ANSIBLE_VERSION}

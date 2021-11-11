FROM centos:7
ENV ANSIBLE_VERSION="2.9.16"
ENV ANSIBLE_LINT_VERSION="4.2.0"
WORKDIR /etc/ansible 

LABEL org.opencontainers.image.title='sedunne/docker-centos7-ansible'
LABEL org.opencontainers.image.description='CentOS 7 Systemd Ansible Image'
LABEL org.opencontainers.image.url='https://github.com/sedunne/docker-centos7-ansible'
LABEL org.opencontainers.image.authors='Stephen Dunne <stephen@f914.net>'
LABEL org.opencontainers.image.version=${ANSIBLE_VERSION}

## setup dependencies
RUN yum makecache fast \
    && yum -y install deltarpm epel-release initscripts \
    && yum -y install sudo which git python python-pip \
    && yum clean all

## install ansible and ansible-lint
RUN pip install ansible==${ANSIBLE_VERSION} ansible-lint==${ANSIBLE_LINT_VERSION}

# Disable requiretty, and add local inventory file
RUN sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/' /etc/sudoers && \
    echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts

STOPSIGNAL SIGRTMIN+3
CMD ["/usr/sbin/init"]

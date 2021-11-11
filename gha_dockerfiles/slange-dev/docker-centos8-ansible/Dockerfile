FROM centos:8
LABEL maintainer="slange-dev"
ENV container=docker

ENV pip_packages "ansible"
ENV python_version "python3.8"

# Install systemd -- See https://hub.docker.com/_/centos/
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

# Install requirements.
RUN yum -y install rpm centos-release dnf-plugins-core \
 && yum -y update \
 && yum -y upgrade \
 && yum -y config-manager --set-enabled powertools \
 && yum -y install \
      sudo \
      epel-release \
      initscripts \
      which \
      hostname \
      libyaml-devel \
      $python_version \
      python3-pip \
      python3-pyyaml \
 && yum clean all

# Upgrade pip to latest version.
RUN pip3 install --user --upgrade pip

# Install Ansible via Pip.
RUN pip3 install $pip_packages

# Disable requiretty.
RUN sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers

# Install Ansible inventory file.
RUN mkdir -p /etc/ansible
RUN echo -e '[local]\nlocalhost ansible_connection=local ansible_python_interpreter=/usr/bin/python3' > /etc/ansible/hosts

# Add volume and systemd
VOLUME ["/sys/fs/cgroup"]
CMD ["/usr/lib/systemd/systemd"]

FROM centos:latest
MAINTAINER major@redhat.com

# Get required RPM packages
RUN yum -y upgrade
RUN yum --quiet --assumeyes install bison flex yum-utils git python \
    python-devel openssl-devel libffi-devel wget
RUN yum-builddep --quiet --assumeyes kernel-*
RUN yum clean all && rm -rf /var/cache/yum/*

# Install Ansible
RUN wget --quiet --output-document=/opt/get-pip.py https://bootstrap.pypa.io/get-pip.py
RUN python /opt/get-pip.py
RUN pip install ansible

# Run playbook
COPY run.sh /run.sh
CMD /bin/bash /run.sh

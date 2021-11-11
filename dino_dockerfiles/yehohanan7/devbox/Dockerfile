VERSION 0.0.3
FROM ubuntu:14.04

RUN apt-get -qq update

# Install prereqs
RUN apt-get --no-install-recommends -y install \
    build-essential \
    openssh-client \
    ca-certificates \
    curl \
    git \
    libicu-dev \
    libmozjs185-dev \
    python \
    python-software-properties \
    software-properties-common
    

# Build and install ansible
RUN apt-get install -y python-yaml python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools python-pkg-resources git python-pip
RUN mkdir /etc/ansible/
RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts
RUN mkdir /opt/ansible/
RUN git clone http://github.com/ansible/ansible.git /opt/ansible/ansible
WORKDIR /opt/ansible/ansible
RUN git submodule update --init
ENV PATH /opt/ansible/ansible/bin:/bin:/usr/bin:/sbin:/usr/sbin
ENV PYTHONPATH /opt/ansible/ansible/lib
ENV ANSIBLE_LIBRARY /opt/ansible/ansible/library


# Provision the dev box
RUN git clone http://github.com/yehohanan7/scm.git /tmp/scm
WORKDIR /tmp/scm
RUN ansible-playbook ansible/site.yml -i hosts
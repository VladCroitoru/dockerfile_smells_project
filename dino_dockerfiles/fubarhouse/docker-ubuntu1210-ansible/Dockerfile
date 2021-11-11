FROM ubuntu:12.10
MAINTAINER Karl Hepworth

# Convert sources to legacy.
RUN sed -i.bak -r 's/(archive|security).ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

# Install dependencies.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       curl python-pip make git \
       python-dev python-yaml python-paramiko python-jinja2 python-httplib2 \
       python-software-properties software-properties-common \
       rsyslog sudo build-essential gcc rsync openssh-server libssl-dev libffi-dev zip wget \
    && rm -Rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean
RUN pip install setuptools

# Upgrade python
RUN wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz \
    && tar zxf ./Python-2.7.13.tgz \
    && cd Python-2.7.13 \
    && ./configure \
    && make \
    && make install \
    && rm -f ../Python-2.7.13.tgz

RUN sed -i 's/^\($ModLoad imklog\)/#\1/' /etc/rsyslog.conf
#ADD etc/rsyslog.d/50-default.conf /etc/rsyslog.d/50-default.conf

# Install Ansible
RUN pip install urllib3 pyOpenSSL ndg-httpsclient pyasn1 ansible cryptography

COPY initctl_faker .
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker /sbin/initctl

# Install Ansible inventory file
RUN mkdir /etc/ansible
RUN echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

# Report some information
RUN python --version
RUN ansible --version
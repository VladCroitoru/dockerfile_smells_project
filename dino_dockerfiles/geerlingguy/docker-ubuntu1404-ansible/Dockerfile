FROM ubuntu:14.04
LABEL maintainer="Jeff Geerling"

ENV pip_packages "ansible"

# Install dependencies and upgrade Python.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
       python2.7 \
    && ln -s /usr/bin/python2.7 /usr/bin/python \
    && rm -Rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

# Install Ansible via Pip.
ADD https://bootstrap.pypa.io/get-pip.py .
RUN /usr/bin/python2.7 get-pip.py \
  && pip install $pip_packages

# Install Ansible inventory file.
RUN mkdir -p /etc/ansible
RUN echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

# Workaround for pleaserun tool that Logstash uses
RUN rm -rf /sbin/initctl && ln -s /sbin/initctl.distrib /sbin/initctl

VOLUME ["/sys/fs/cgroup"]
CMD ["/sbin/init"]

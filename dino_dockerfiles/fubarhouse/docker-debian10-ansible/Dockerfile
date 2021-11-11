FROM debian:buster
MAINTAINER Karl Hepworth

ENV DEBIAN_FRONTEND noninteractive

# Install dependencies.
RUN apt-get update \
    && apt-get install -y \
    --no-install-recommends \
    sudo curl gnupg2

# Install Python dependencies.
RUN apt-get install -y --no-install-recommends \
    build-essential libffi-dev libssl-dev python-dev \
    zlib1g-dev libncurses5-dev systemd python-setuptools curl

# Install PIP & Ansible
RUN apt-get install -y python-pip \
    && pip install urllib3 pyOpenSSL ndg-httpsclient pyasn1 cryptography \
    && pip install ansible

# General clean-up
RUN rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

COPY initctl_faker .
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker /sbin/initctl

# Install Ansible inventory file
RUN mkdir -p /etc/ansible \
    && echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

# Report some information
RUN python --version
RUN ansible --version
# Debian Stretch (9) base docker image used for testing ansible roles & playbooks.
FROM debian:stretch
LABEL maintainer="Pedro Gomes"

ENV DEBIAN_FRONTEND noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends sudo systemd build-essential libffi-dev libssl-dev python-pip python-dev python-setuptools python-wheel && \
    rm -rf /var/lib/apt/lists/* && \
    rm -Rf /usr/share/doc && rm -Rf /usr/share/man && \
    apt-get clean

RUN pip install ansible cryptography

RUN useradd -ms /bin/bash deploy

COPY initctl_faker .
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker /sbin/initctl

# Install Ansible inventory file
RUN mkdir -p /etc/ansible \
    && echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

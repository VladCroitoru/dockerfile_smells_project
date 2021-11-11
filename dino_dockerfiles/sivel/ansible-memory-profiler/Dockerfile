FROM debian:stretch-slim

MAINTAINER Matt Martz matt@sivel.net

RUN set -x && \
    \
    apt-get clean && \
    apt-get update && \
    apt-get install -y --no-install-recommends cgroup-tools python-pip python-setuptools sudo && \
    \
    pip install -U pip && \
    hash -r pip && \
    pip install jinja2 PyYAML paramiko cryptography setuptools && \
    \
    useradd -m -s /bin/bash ansible && \
    echo ansible:ansible | /usr/sbin/chpasswd && \
    \
    rm -rf /var/lib/apt/lists/*

COPY cgroup_memory_recap.py /usr/share/ansible/plugins/callback/cgroup_memory_recap.py
COPY cgcreate /etc/sudoers.d
COPY docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

USER ansible
CMD []

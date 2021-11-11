FROM ubuntu:16.04
MAINTAINER Robert Powers <robert@synaxa.io>

ENV PATH /ansible/bin:$PATH
ENV PYTHONPATH /ansible/lib
ENV ANSIBLE_LOG_PATH=/logs/ansible.log
ENV ANSIBLE_DEBUG FALSE
ENV ANSIBLE_HOST_KEY_CHECKING False

RUN apt-get update && \
    apt-get install -y python python-pip git vim && \
    \
    \
    pip install ansible==2.4.0 && \
    mkdir /ansible /logs /ansible/playbooks /etc/ansible && \
    echo '[local]\nlocalhost' > /etc/ansible/hosts

WORKDIR /ansible/playbooks

ENTRYPOINT [ "ansible", "--version" ]
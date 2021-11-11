FROM ubuntu:18.04

MAINTAINER "Riley Schuit"

# Allows installation of tzdata to run unattended
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get -y install \
  curl \
  ansible \
  python3-pip \
  build-essential libssl-dev libffi-dev python3-pip python3-dev gnupg

RUN apt-get install ca-certificates

RUN pip3 install \
  bigsuds \
  f5-icontrol-rest \
  f5-sdk

# Ansible specific environment variables
ENV ANSIBLE_HOST_KEY_CHECKING="False" \
    ANSIBLE_LIBRARY="/ansible/library" \
    ANSIBLE_RETRY_FILES_ENABLED="False" \
    INTERPRETER_PYTHON="/usr/bin/python3" \
    PATH="/ansible/bin:$PATH" \
    PYTHONPATH="/ansible/lib"

WORKDIR /ansible/playbooks

ENTRYPOINT ["ansible-playbook"]

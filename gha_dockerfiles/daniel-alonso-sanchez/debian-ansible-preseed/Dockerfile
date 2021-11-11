FROM alpine:3.6


# Default version of Ansible
ARG ANSIBLE_VERSION=2.9.2


# == Setup container
#
ENTRYPOINT ["/usr/bin/ansible-playbook"]
CMD ["-h"]


# == Configure runtime environment
#
ENV ANSIBLE_GATHERING=smart \
    ANSIBLE_HOST_KEY_CHECKING=False \
    ANSIBLE_RETRY_FILES_ENABLED=False \
    ANSIBLE_ROLES_PATH=/ansible/playbooks/roles \
    ANSIBLE_SSH_PIPELINING=True

# Setup Ansible Layout
COPY files/hosts /etc/ansible/hosts

RUN mkdir -p /ansible/playbooks &&  mkdir -p /ansible/plugins

WORKDIR /ansible/playbooks


# == Install Ansible dependencies
#
RUN \
  echo '* Installing OS Dependencies' \
  && apk add --update --no-cache \
    build-base \
    curl openssh-client tar \
    python python-dev py-pip \
    libffi-dev openssl-dev sshpass \
  && echo '* Installing Ansible via PIP' \
  && pip install --upgrade \
    pip \
    docker \
    ansible==${ANSIBLE_VERSION} \
  && echo '* Cleaning unneeded packages' \ 
  && apk del \
    build-base \
    libffi-dev openssl-dev \
    python-dev

RUN curl https://files.pythonhosted.org/packages/67/65/612aa75b9b16ef4d81d1f840ce59f01a7b348ee54df8966be0aeea7e7848/mitogen-0.2.9.tar.gz -o /ansible/plugins/mitogen-0.2.9.tar.gz && tar -C /ansible/plugins  -xvzf /ansible/plugins/mitogen-0.2.9.tar.gz &&  rm /ansible/plugins/mitogen-0.2.9.tar.gz

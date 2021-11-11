FROM gliderlabs/alpine

RUN \
  apk-install \
  bash \
  curl \
  openssh-client \
  python \
  python-dev \
  py-boto \
  py-dateutil \
  py-httplib2 \
  py-jinja2 \
  py-paramiko \
  py-pip \
  py-setuptools \
  py-yaml \
  openssl \
  gcc \
  libc-dev \
  tar && \
  pip install --upgrade pip python-keyczar && \
  rm -rf /var/cache/apk/*

RUN mkdir /etc/ansible/ /ansible
RUN echo "[local]" >> /etc/ansible/hosts && \
  echo "localhost" >> /etc/ansible/hosts

RUN \
  curl -fsSL https://releases.ansible.com/ansible/ansible-2.6.2.tar.gz -o ansible.tar.gz && \
  tar -xzf ansible.tar.gz -C ansible --strip-components 1 && \
  rm -fr ansible.tar.gz /ansible/docs /ansible/examples /ansible/packaging

RUN mkdir -p /ansible/playbooks
WORKDIR /ansible/playbooks

ENV ANSIBLE_GATHERING smart
ENV ANSIBLE_HOST_KEY_CHECKING false
ENV ANSIBLE_RETRY_FILES_ENABLED false
ENV ANSIBLE_ROLES_PATH /ansible/playbooks/roles
ENV ANSIBLE_SSH_PIPELINING True
ENV PATH /ansible/bin:$PATH
ENV PYTHONPATH /ansible/lib

# overwrite this with 'CMD []' in a dependent Dockerfile
CMD ["/bin/bash"]

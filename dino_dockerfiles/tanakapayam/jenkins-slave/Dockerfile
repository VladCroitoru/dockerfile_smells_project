# Creates a souped-up Jenkins-Slave build node, including the following:
#
# - ansible, +ansible-playbook, +ansible-vault
# - curl
# - docker
# - gcloud, +beta, +kubectl, +pubsub-emulator
# - git
# - go
# - jq
# - make
# - maven
# - postgresql
# - python

# jessie
FROM jenkinsci/jnlp-slave

USER root
WORKDIR /home/jenkins

ARG DOCKER_PKG=docker-ce
ARG GO_TARBALL=https://storage.googleapis.com/golang/go1.8.3.linux-amd64.tar.gz
ARG MAVEN_PKG=maven
ARG POSTGRESQL_PKG=postgresql-9.5
ARG NODEJS_VERSION=8.x

ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1
ENV PATH /usr/local/go/bin:/opt/google-cloud-sdk/bin:/opt/ansible/bin:$PATH
ENV PYTHONPATH /opt/ansible/lib
ENV ANSIBLE_LIBRARY /opt/ansible/library

RUN set -ex \
    && apt-get -qq update \
    && DEBIAN_FRONTEND=noninteractive apt-get -yqq install --no-install-recommends \
        apt-utils \
    && apt-get -yqq purge \
        docker* \
    && DEBIAN_FRONTEND=noninteractive apt-get -yqq install \
        apt-transport-https \
        ca-certificates \
        curl \
        git \
        jq \
        lsb-release \
        make \
        python-httplib2 \
        python-jinja2 \
        python-keyczar \
        python-paramiko \
        python-pip \
        python-pkg-resources \
        python-setuptools \
        python-yaml \
    &&  echo "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
        > /etc/apt/sources.list.d/docker.list \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
        | apt-key add - \
    &&  echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" \
        > /etc/apt/sources.list.d/pgdg.list \
    && curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc \
        | apt-key add - \
    && curl -fsSL https://deb.nodesource.com/setup_${NODEJS_VERSION} \
        | bash - \
    && apt-get -qq update \
    && DEBIAN_FRONTEND=noninteractive apt-get -yqq install \
        $DOCKER_PKG \
        $MAVEN_PKG \
        $POSTGRESQL_PKG \
        nodejs \
    && curl -sO ${GO_TARBALL} \
    && tar -C /usr/local -xzf $(basename ${GO_TARBALL}) \
    && rm -f $(basename ${GO_TARBALL}) \
    && curl -s https://sdk.cloud.google.com \
        | bash >/dev/null 2>&1 \
    && mv google-cloud-sdk /opt \
    && gcloud components install beta kubectl pubsub-emulator >/dev/null 2>&1 \
    && mkdir -p /etc/ansible /opt/ansible \
    && printf "[local]\nlocalhost\n" \
        > /etc/ansible/hosts \
    && cd /opt \
    && git clone http://github.com/ansible/ansible.git \
    && cd /opt/ansible \
    && git submodule update --init \
    && apt-get clean \
    && rm -rf \
        * \
        .bash_logout \
        .bashrc \
        .config \
        .profile \
        /root/.??* \
        /tmp/* \
        /var/lib/apt/lists/* \
        /var/tmp/*

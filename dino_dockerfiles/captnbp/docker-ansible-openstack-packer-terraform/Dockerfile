FROM alpine:latest

ENV TERRAFORM_VERSION 0.11.1
ENV PACKER_VERSION 1.1.2
ENV FAAS_CLI_VERSION 0.5.0

RUN apk add -U python3 py3-pip openssl ca-certificates python3-dev libffi-dev openssl-dev build-base linux-headers terraform docker curl coreutils

RUN echo "===> Installing sudo to emulate normal OS behavior..."  && \
    apk --update add sudo                                         && \
    \
    \
    echo "===> Adding Python runtime..." && \
    apk --update add python3 py3-pip openssl ca-certificates openssh openssh-client && \
    apk --update add --virtual build-dependencies python3-dev libffi-dev openssl-dev build-base linux-headers && \
    pip3 install --upgrade pip cffi && \
    echo "===> Installing Ansible..." && \
    pip3 install ansible              && \
    echo "===> Installing Openstack clients..." && \
    pip3 install python-novaclient python-openstackclient python-cinderclient python-glanceclient python-neutronclient shade datadog && \
    echo "===> Removing package list..." && \
    apk del build-dependencies           && \
    rm -rf /var/cache/apk/*              && \
    echo "===> Adding hosts for convenience..." && \
    mkdir -p /etc/ansible                       && \
    echo 'localhost' > /etc/ansible/hosts

RUN wget https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip && \
	unzip packer_${PACKER_VERSION}_linux_amd64.zip && \
	rm packer_${PACKER_VERSION}_linux_amd64.zip && \
	mv packer /usr/local/bin/packer
RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
	unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
	rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
	mv terraform /usr/local/bin/terraform

ADD https://github.com/openfaas/faas-cli/releases/download/${FAAS_CLI_VERSION}/faas-cli /usr/local/bin/faas-cli
RUN chmod +x /usr/local/bin/faas-cli

FROM debian:sid
MAINTAINER jfcoz
ENV TERRAFORM_VERSION=0.7.0
ADD ./deb/ansible_1.9.4-1_all.deb /ansible_1.9.4-1_all.deb
RUN apt-get update \
    && apt-get install -y wget zip git openssh-client python-cryptography python-openssl procps python-boto sudo make \
    && mkdir /terraform \
    && cd /terraform \
    && wget -q https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin/ \
    && rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && apt-get install -y /ansible_1.9.4-1_all.deb \
    && rm /ansible_1.9.4-1_all.deb

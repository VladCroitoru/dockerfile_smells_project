FROM ubuntu:16.04

MAINTAINER Matthew Titmus <matthew.titmus@gmail.com>

ARG ANSIBLE_VERSION=2.1.1.0-1~ubuntu16.04.1
ARG AWSCLI_VERSION=1.12.1
ARG HELM_VERSION=2.8.2
ARG ISTIO_VERSION=0.6.0
ARG KOPS_VERSION=1.9.0
ARG KUBECTL_VERSION=1.10.1
ARG TERRAFORM_VERSION=0.11.0

# Install generally useful things
#
RUN apt-get update                                          \
  && apt-get -y --force-yes install --no-install-recommends \
    curl                                                    \
    dnsutils                                                \
    git                                                     \
    jq                                                      \
    net-tools                                               \
    ssh                                                     \
    telnet                                                  \
    unzip                                                   \
    vim                                                     \
    wget                                                    \
  && apt-get clean                                          \
  && apt-get autoclean                                      \
  && apt-get autoremove                                     \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install AWS CLI
#
RUN apt-get update                                          \
  && apt-get -y --force-yes install                         \
    python-pip                                              \
  && pip install awscli==${AWSCLI_VERSION}                  \
  && apt-get clean                                          \
  && apt-get autoclean                                      \
  && apt-get autoremove                                     \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Ansible
#
RUN apt-get update                                          \
  && pip install boto                                       \
  && apt-get -y --force-yes install --no-install-recommends \
    software-properties-common                              \
  && apt-add-repository -y ppa:ansible/ansible              \
  && apt-get update                                         \
  && apt-get -y --force-yes install --no-install-recommends \
    ansible=${ANSIBLE_VERSION}                              \
  && apt-get clean                                          \
  && apt-get autoclean                                      \
  && apt-get autoremove                                     \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Terraform
#
RUN wget -O terraform.zip https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
  && unzip terraform.zip \
  && mv terraform /usr/local/bin/terraform \
  && chmod +x /usr/local/bin/terraform \
  && rm terraform.zip

# Install kubectl
#
ADD https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl /usr/local/bin/kubectl
RUN chmod +x /usr/local/bin/kubectl

# Install Kops
#
ADD https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-linux-amd64 /usr/local/bin/kops
RUN chmod +x /usr/local/bin/kops
ENV ANSIBLE_VAULT_PASSWORD_FILE="/home/kops/.avp"

# Install Helm
#
RUN wget -O helm.tar.gz https://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz \
	&& tar xfz helm.tar.gz \
	&& mv linux-amd64/helm /usr/local/bin/helm \
	&& chmod +x /usr/local/bin/helm \
	&& rm -Rf linux-amd64 \
	&& rm helm.tar.gz

# Install Istioctl
#
RUN wget -O istio.tar.gz https://github.com/istio/istio/releases/download/${ISTIO_VERSION}/istio-${ISTIO_VERSION}-linux.tar.gz \
  && tar xfz istio.tar.gz \
  && mv istio-${ISTIO_VERSION}/bin/istioctl /usr/local/bin/istioctl \
  && chmod +x /usr/local/bin/istioctl \
  && rm -Rf istio-${ISTIO_VERSION} \
  && rm istio.tar.gz

# Create default user "kops"
#
RUN useradd -ms /bin/bash kops
WORKDIR /home/kops
ADD kube_ps1 /home/kops/.bash_aliases
USER kops

# Ensure the prompt doesn't break if we don't mount the ~/.kube directory
#
RUN mkdir /home/kops/.kube \
  && touch /home/kops/.kube/config

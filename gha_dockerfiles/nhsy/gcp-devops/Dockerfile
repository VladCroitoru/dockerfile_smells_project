FROM alpine:latest

LABEL name=gcp-devops

ARG GCLOUD_VERSION=358.0.0
ARG HELM_VERSION=3.7.0
ARG TERRAFORM_VERSION=1.0.8
ARG TERRAGRUNT_VERSION=0.32.4
ARG PACKER_VERSION=1.7.6

ENV CLOUDSDK_PYTHON=python3
ENV PATH /usr/lib/google-cloud-sdk/bin:$PATH
ENV TF_PLUGIN_CACHE_DIR=/opt/terraform/plugins-cache
ENV TERRAGRUNT_DOWNLOAD=/opt/terragrunt/cache

RUN \
  apk --no-cache add \
    ansible \
    bash \
    bash-completion \
    curl \
    groff \
    git \
    jq \
    less \
    libc6-compat \
    make \
    openssh-client \
    python3 \
    py3-pip \
    py3-crcmod \
    tree \
    vim \
    wget \
    unzip \
    && \
  \
  pip3 install --upgrade pip && \
  \
  wget -q -O /tmp/google-cloud-sdk.tgz https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${GCLOUD_VERSION}-linux-x86_64.tar.gz && \
  tar xzf /tmp/google-cloud-sdk.tgz -C /usr/lib/ && \
  rm /tmp/google-cloud-sdk.tgz && \
  ln -s /lib /lib64 && \
  gcloud config set core/disable_usage_reporting true && \
  gcloud config set component_manager/disable_update_check true && \
  gcloud config set metrics/environment github_docker_image && \
  gcloud components install beta kubectl docker-credential-gcr --quiet && \
  \
  # Cleanup \
  rm -rf /tmp/* && \
  rm -rf /var/cache/apk/* && \
  rm -rf /var/tmp/*

RUN \
  wget -qO /tmp/terraform.zip https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
  unzip -q /tmp/terraform.zip -d /tmp && \
  chmod +x /tmp/terraform && \
  chown root.root /tmp/terraform && \
  mv /tmp/terraform /usr/local/bin && \
  \
  wget -qO /tmp/terragrunt https://github.com/gruntwork-io/terragrunt/releases/download/v${TERRAGRUNT_VERSION}/terragrunt_linux_amd64 && \
  chmod +x /tmp/terragrunt && \
  chown root.root /tmp/terragrunt && \
  mv /tmp/terragrunt /usr/local/bin && \
  \
  wget -qO /tmp/packer.zip https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip && \
  unzip -q /tmp/packer.zip -d /tmp && \
  chmod +x /tmp/packer && \
  chown root.root /tmp/packer && \
  mv /tmp/packer /usr/local/bin && \
  \
  wget -qO /tmp/helm.tgz https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
  tar xzvf /tmp/helm.tgz -C /tmp --strip-components 1 linux-amd64/helm && \
  chmod +x /tmp/helm && \
  chown root.root /tmp/helm && \
  mv /tmp/helm /usr/local/bin && \
  \
  mkdir -p ${TF_PLUGIN_CACHE_DIR} && \
  mkdir -p ${TERRAGRUNT_DOWNLOAD} && \
  ansible --version && \
  helm version --client && \
  terraform version && \
  terragrunt -version && \
  packer version && \
  \
  # Cleanup \
  rm -rf /tmp/* && \
  rm ~/.wget-hsts && \
  rm -rf $(find /usr/lib/google-cloud-sdk/ -regex ".*/__pycache__") && \
  rm -rf /usr/lib/google-cloud-sdk/.install/.backup

# Customisations
COPY *.sh /tmp/
RUN \
  adduser -Ds /bin/bash devops && \
  \
  chmod -R 777 ${TF_PLUGIN_CACHE_DIR} && \
  chmod -R 777 ${TERRAGRUNT_DOWNLOAD} && \
  \
  . /tmp/20-bashrc.sh && \
  \
  # Cleanup \
  rm -rf /tmp/*

ENTRYPOINT ["/bin/bash"]

WORKDIR /work

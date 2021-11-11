FROM golang:1.9 AS provider
RUN go get -d github.com/andrewrynhard/terraform-provider-helm
WORKDIR $GOPATH/src/github.com/andrewrynhard/terraform-provider-helm
RUN go build -o /tmp/terraform-provider-helm .

FROM debian:buster-slim
LABEL maintainer="Andrew Rynhard <andrew.rynhard@logicmonitor.com>"

ENV TERRAFORM_VERSION="0.11.3"
ENV KUBERNETES_VERSION="v1.9.3"
ENV HELM_VERSION="v2.8.2"

RUN apt-get -y update \
    && apt-get -y install --no-install-recommends \
    ca-certificates \
    curl \
    git \
    gnupg2 \
    openssh-client \
    unzip \
    vim \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LO https://download.opensuse.org/repositories/shells:fish:release:2/Debian_8.0/Release.key \
    && apt-key add - < Release.key \
    && apt-get update

RUN echo 'deb http://download.opensuse.org/repositories/shells:/fish:/release:/2/Debian_9.0/ /' > /etc/apt/sources.list.d/fish.list \
    && apt-get update \
    && apt-get install -y fish

# Helm Terraform Provider
COPY --from=provider /tmp/terraform-provider-helm /usr/local/bin/

# Terraform
RUN curl -L https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -o /tmp/terraform.zip \
    && unzip /tmp/terraform.zip \
    && mv terraform /usr/local/bin/ \
    && rm /tmp/terraform.zip

# Kubernetes
RUN curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBERNETES_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
    && curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBERNETES_VERSION}/bin/linux/amd64/kubeadm -o /usr/local/bin/kubeadm

# Helm
RUN curl -L https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz | tar -xz -C /tmp \
    && mv /tmp/linux-amd64/helm /usr/local/bin/helm \
    && chmod +x /usr/local/bin/* \
    && rm -rf /tmp/linux-amd64

# .bashrc
RUN echo '{ eval $(ssh-agent); ssh-add; ssh-add ~/.kube/assets/ssh/id_rsa; } &>/dev/null' >> ~/.bashrc

RUN ln -fs /bin/bash /bin/sh

WORKDIR /src

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

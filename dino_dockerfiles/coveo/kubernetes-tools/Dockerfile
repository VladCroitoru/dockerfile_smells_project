FROM python:3.8-alpine

# Install dep & upgrade pip
RUN apk add --no-cache git curl ca-certificates bash jq build-base && \
  pip install -U pip


ARG kube_version=1.11.10
ARG kops_version=1.11.1
ARG helm_version=2.9.1


# Install kubectl
RUN curl -s -L https://storage.googleapis.com/kubernetes-release/release/v${kube_version}/bin/linux/amd64/kubectl > /usr/local/bin/kubectl && \
  chmod +x /usr/local/bin/kubectl

# Install kops
RUN curl -s -L https://github.com/kubernetes/kops/releases/download/${kops_version}/kops-linux-amd64 >  /usr/local/bin/kops && \
  chmod +x /usr/local/bin/kops

# Install helm
RUN curl -s -L https://kubernetes-helm.storage.googleapis.com/helm-v${helm_version}-linux-amd64.tar.gz | tar xzv && \
  chmod +x ./linux-amd64/helm && \
  mv ./linux-amd64/helm /usr/local/bin/helm && \
  mkdir -p $(helm home)/plugins

# Install helm-template
RUN helm plugin install https://github.com/technosophos/helm-template

# Install aws-cli
RUN pip install awscli aws-sudo

RUN addgroup -S -g 1001 jenkins && adduser -u 1001 -D -S jenkins
USER jenkins
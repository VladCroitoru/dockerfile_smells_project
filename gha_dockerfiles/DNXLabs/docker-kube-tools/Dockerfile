FROM alpine:3.13

ENV KUBECTL_VERSION=1.22.3
ENV HELM_VERSION=3.7.1
ENV VELERO_VERSION=1.7.0
ENV ARGOCD_VERSION=2.1.6
ENV OCTANT_VERSION=0.24.0

VOLUME ["/work"]

WORKDIR /work

COPY scripts /opt/scripts

ENV PATH "$PATH:/opt/scripts"

RUN apk --no-cache update && \
    apk --no-cache add \
        bash \
        ca-certificates \
        git \
        openssl \
        unzip \
        gzip \
        zip \
        curl \
        make \
        tar \
        python3 \
        py3-pip \
        py3-setuptools \
        groff \
        less \
        jq \
        gettext-dev \
        g++ \
        libc6-compat \
        libstdc++ && \
    python3 -m pip --no-cache-dir install --upgrade pip && \
    python3 -m pip --no-cache-dir install --upgrade awscli && \
    update-ca-certificates && \
    rm -rf /var/tmp/ && \
    rm -rf /tmp/* && \
    rm -rf /var/cache/apk/*

# Kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl

# Helm
RUN curl -LO https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz  && \
    tar -zxvf helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
    chmod +x linux-amd64/helm && \
    mv linux-amd64/helm /usr/local/bin/helm && \
    rm -rf linux-amd64 && rm -rf helm-v${HELM_VERSION}-linux-amd64.tar.gz

# Velero
RUN curl -LO https://github.com/vmware-tanzu/velero/releases/download/v${VELERO_VERSION}/velero-v${VELERO_VERSION}-linux-amd64.tar.gz && \
    tar -xvzf velero-v${VELERO_VERSION}-linux-amd64.tar.gz && \
    chmod +x ./velero-v${VELERO_VERSION}-linux-amd64/velero && \
    mv ./velero-v${VELERO_VERSION}-linux-amd64/velero /usr/local/bin/velero && \
    rm -rf ./velero-v${VELERO_VERSION}-linux-amd64 && rm -rf velero-v${VELERO_VERSION}-linux-amd64.tar.gz

# Argo CD
RUN curl --silent --location -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/download/v${ARGOCD_VERSION}/argocd-linux-amd64 && \
    chmod +x /usr/local/bin/argocd

# kyml
RUN curl -sfL -o /usr/local/bin/kyml https://github.com/frigus02/kyml/releases/download/v20190906/kyml_20190906_linux_amd64 && \
    chmod +x /usr/local/bin/kyml

# octant
RUN curl -LO https://github.com/vmware-tanzu/octant/releases/download/v${OCTANT_VERSION}/octant_${OCTANT_VERSION}_Linux-64bit.tar.gz && \
    tar -xvzf octant_${OCTANT_VERSION}_Linux-64bit.tar.gz && \
    chmod +x ./octant_${OCTANT_VERSION}_Linux-64bit/octant && \
    mv ./octant_${OCTANT_VERSION}_Linux-64bit/octant /usr/local/bin/octant && \
    rm -rf ./octant_${OCTANT_VERSION}_Linux-64bit/octant && rm -rf octant_${OCTANT_VERSION}_Linux-64bit.tar.gz
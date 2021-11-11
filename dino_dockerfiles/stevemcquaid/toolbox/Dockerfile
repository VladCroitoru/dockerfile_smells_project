FROM ubuntu:18.04
RUN apt-get update && apt-get install -y aptitude
RUN apt-get install -y \
    dialog \
    apt-utils
RUN apt-get install -y \
    curl \
    arping \
    arp-scan \
    bind9-host \
    dhcping \
    dnsutils \
    git \
    iptables \
    iputils-ping \
    mtr \
    nano \
    netcat \
    net-tools \
    nmap \
    tcpdump \
    telnet \
    tftp-hpa \
    traceroute \
    vim \
    wget
RUN apt-get install -y apt-transport-https

# Install k8s tools
ARG EXTRACT_PATH="/tmp/extract"
RUN mkdir -p ${EXTRACT_PATH}
ARG GO111MODULE=on
# Install helm
ARG HELM_VERSION="2.16.5"
# ARG HELM_VERSION="2.14.3"
RUN curl -LO https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz \
    && tar -C ${EXTRACT_PATH} --strip-components=1 -xzf helm-v${HELM_VERSION}-linux-amd64.tar.gz \
    && mv ${EXTRACT_PATH}/helm /usr/local/bin/helm
ENV PATH=/usr/local/bin/:$PATH
# Install helm3
ARG HELM_VERSION="3.2.1"
RUN curl -LO https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz \
    && tar -C ${EXTRACT_PATH} --strip-components=1 -xzf helm-v${HELM_VERSION}-linux-amd64.tar.gz \
    && mv ${EXTRACT_PATH}/helm /usr/local/bin/helm3
ENV PATH=/usr/local/bin/:$PATH
# install kubernetes
ARG KUBECTL_VERSION="v1.18.0"
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl  \
  && chmod +x kubectl \
  && mv kubectl /usr/local/bin/kubectl

# Trap shell to keep it running!
CMD exec /bin/sh -c "trap : TERM INT; (while true; do sleep 1000; done) & wait"

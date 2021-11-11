FROM ubuntu:16.04

ARG KUBERNETES_VERSION=v1.16.10

ENV DEBIAN_FRONTEND=noninteractive \
    container=docker \
    KUBERNETES_DOWNLOAD_ROOT=https://storage.googleapis.com/kubernetes-release/release/${KUBERNETES_VERSION}/bin/linux/amd64 \
    KUBERNETES_COMPONENT=kube-controller-manager

RUN set -x \
    && apt-get update \
    && apt install wget apt-transport-https ca-certificates -y \
    && wget -q -O- 'https://download.ceph.com/keys/release.asc' | apt-key add - \
    && echo deb https://download.ceph.com/debian-nautilus/ xenial main | tee /etc/apt/sources.list.d/ceph.list \
    && apt-get update \
    && apt-get install -y \
        ceph-common \
        curl \
    && touch /etc/ceph/ceph.conf /etc/ceph/ceph.keyring \
    && curl -L ${KUBERNETES_DOWNLOAD_ROOT}/${KUBERNETES_COMPONENT} -o /usr/bin/${KUBERNETES_COMPONENT} \
    && chmod +x /usr/bin/${KUBERNETES_COMPONENT} \
    && apt-get purge -y --auto-remove \
        curl \
    && rm -rf /var/lib/apt/lists/*

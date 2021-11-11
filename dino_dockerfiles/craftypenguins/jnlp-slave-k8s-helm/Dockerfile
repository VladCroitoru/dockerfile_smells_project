FROM jenkins/jnlp-slave:3.19-1-alpine
MAINTAINER Kerkhoff Technologies Inc. <linuxsupport@kerkhofftech.ca>

ENV HELM_VERSION v2.8.2
ENV HELM_FILENAME helm-${HELM_VERSION}-linux-amd64.tar.gz
ENV KUBE_LATEST_VERSION="v1.9.6"

USER root
WORKDIR /
RUN apk add --update -t deps curl tar gzip ca-certificates git
RUN curl -L http://storage.googleapis.com/kubernetes-helm/${HELM_FILENAME} | tar zxv -C /tmp \
  && cp /tmp/linux-amd64/helm /usr/local/bin/helm \
  && chmod +x /usr/local/bin/helm

RUN curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
 && chmod +x /usr/local/bin/kubectl

RUN apk del --purge deps \
 && rm /var/cache/apk/* 

USER jenkins
RUN helm init --client-only
WORKDIR /home/jenkins


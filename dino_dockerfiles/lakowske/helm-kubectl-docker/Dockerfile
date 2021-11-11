FROM alpine:3.7

MAINTAINER Seth Lakowske <lakowske@gmail.com>

# Enable SSL
RUN apk --update add ca-certificates wget curl tar git bash docker openssh-client \
    && rm -rf /var/cache/apk/*

# Install kubectl
ENV KUBE_LATEST_VERSION='v1.8.2'

RUN curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
   && chmod +x /usr/local/bin/kubectl
   
# Install Helm
ENV HELM_VERSION v2.7.2
ENV FILENAME helm-${HELM_VERSION}-linux-amd64.tar.gz
ENV HELM_URL https://storage.googleapis.com/kubernetes-helm/${FILENAME}

RUN curl -o /tmp/$FILENAME ${HELM_URL} \
  && tar -zxvf /tmp/${FILENAME} -C /tmp \
    && mv /tmp/linux-amd64/helm /bin/helm \
      && rm -rf /tmp


CMD ["bash"] 
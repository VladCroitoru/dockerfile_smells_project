FROM alpine:3.7

MAINTAINER Sergii Nuzhdin <ipaq.lw@gmail.com>

ENV KUBE_LATEST_VERSION=v1.9.2
ENV HELM_VERSION=v2.7.2
ENV HELM_FILENAME=helm-${HELM_VERSION}-linux-amd64.tar.gz


RUN apk add --update ca-certificates \
 && apk add --update -t deps curl  \
 && apk add --update gettext tar gzip \
 && curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
 && curl -L https://storage.googleapis.com/kubernetes-helm/${HELM_FILENAME} | tar xz && mv linux-amd64/helm /bin/helm && rm -rf linux-amd64 \
 && chmod +x /usr/local/bin/kubectl \
 && apk del --purge deps \
 && rm /var/cache/apk/*

RUN apk add --no-cache curl

RUN apk add --update \
    python \
    python-dev 
    
RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz \
 && mkdir -p /usr/local/gcloud \
 && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
 && /usr/local/gcloud/google-cloud-sdk/install.sh

RUN mkdir -p /opt/google-cloud-sdk/bin \
 && ln -s /usr/local/gcloud/google-cloud-sdk/bin/gcloud /opt/google-cloud-sdk/bin/gcloud

ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

CMD ["helm"]

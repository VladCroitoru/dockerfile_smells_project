ARG AZ_VERSION=2.0.34
FROM microsoft/azure-cli:${AZ_VERSION}

LABEL maintainer="Radek Antoniuk <radek.antoniuk@gmail.com>"
ENV KUBE_VERSION="v1.10.1"

RUN apk add --update ca-certificates \
 && apk add --update -t deps curl \
 && curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
 && chmod +x /usr/local/bin/kubectl \
 && apk del --purge deps \
 && rm /var/cache/apk/*

WORKDIR /root
VOLUME /root

FROM alpine:3.6

MAINTAINER Timothy Stewart <timothystewart6@hotmail.com>

ENV KUBE_LATEST_VERSION="v1.7.6"

RUN mkdir /root/.kube

RUN apk add --update ca-certificates \
 && apk add --update -t deps curl \
 && curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
 && chmod +x /usr/local/bin/kubectl \
 && apk del --purge deps \
 && rm /var/cache/apk/*

RUN chmod a+x /usr/local/bin/kubectl

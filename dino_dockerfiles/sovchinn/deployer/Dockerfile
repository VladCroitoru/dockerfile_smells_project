FROM golang:1.9.1-alpine
LABEL maintainer="Serge Ovchinnikov <sovchinn@gmail.com>"

RUN apk --no-cache add \
        curl \
        openssl

RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | /bin/sh &&\
    curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl &&\
    chmod +x ./kubectl &&\
    mv ./kubectl /usr/local/bin/kubectl

VOLUME ["/files"]
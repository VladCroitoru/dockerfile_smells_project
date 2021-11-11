FROM golang:1.8-alpine
MAINTAINER Nobuhito SATO <nobuhito.sato@gmail.com>

ENV SDK=https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip \
    PACKAGES="curl unzip" \
    CLOUD_SDK=/google-cloud-sdk \
    PATH=/google-cloud-sdk/bin:${PATH} \
    GOROOT=/google-cloud-sdk/platform/google_appengine/goroot-1.8 \
    GOPATH=/google-cloud-sdk/platform/google_appengine/gopath

RUN apk add --update --no-cache gcc musl-dev git python ${PACKAGES} && \
    curl -fo /tmp/gae.zip ${SDK} && unzip -q /tmp/gae.zip -d /tmp/ && mv /tmp/google-cloud-sdk ${CLOUD_SDK} && \
    ${CLOUD_SDK}/install.sh --usage-reporting=true --path-update=true --disable-installation-options --bash-completion=false && \
    yes | gcloud components install app-engine-go && \
    chmod 755 ${CLOUD_SDK}/platform/google_appengine/goapp && \
    apk del ${PACKAGES} --no-cache && rm -rf /tmp/* /var/cache/apk/*

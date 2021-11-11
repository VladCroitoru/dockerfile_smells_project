FROM golang:1.9.1-alpine
LABEL maintainer="Serge Ovchinnikov <sovchinn@gmail.com>"

ENV CLOUD_SDK_VERSION 174.0.0

ENV PATH $PATH:/usr/local/google-cloud-sdk/bin/

RUN apk --no-cache add \
        bash \
        curl \
        git \
        python \
        py-crcmod \
        libc6-compat \
        openssh-client

ADD https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-174.0.0-linux-x86_64.tar.gz .
RUN tar -xvzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz -C /usr/local/ &&\
    rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz &&\
    gcloud config set core/disable_usage_reporting true &&\
    gcloud config set component_manager/disable_update_check true &&\
    gcloud components install kubectl

VOLUME ["/files"]
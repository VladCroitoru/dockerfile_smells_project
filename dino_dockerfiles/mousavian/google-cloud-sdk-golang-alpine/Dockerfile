FROM golang:1.8.3-alpine3.5

LABEL maintainer="Rahman Mousavian <mousavian.rahman@gmail.com>"

ENV CLOUD_SDK_VERSION 170.0.1
ENV GOLANG_VERSION 1.8.3
ENV PATH /google-cloud-sdk/bin:$PATH

RUN apk --no-cache add \
        gcc \
        musl-dev \
        curl \
        python \
        py-crcmod \
        bash \
        libc6-compat \
        openssh-client \
        git

RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz

RUN tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz -C / && \
    rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    ln -s /lib /lib64 && \
    gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    gcloud config set metrics/environment github_docker_image && \
    gcloud components install app-engine-go --quiet && \
    ln -s /google-cloud-sdk/platform/google_appengine/goapp /google-cloud-sdk/bin/ && \
    chmod +x /google-cloud-sdk/bin/goapp

VOLUME ["/root/.config"]

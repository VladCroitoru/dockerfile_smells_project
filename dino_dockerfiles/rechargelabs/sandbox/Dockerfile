# Use latest Ubuntu LTS minimum
FROM ubuntu:18.04

ARG TZ=America/Los_Angeles
ARG DEBIAN_FRONTEND=noninteractive

ARG CLOUD_SDK_VERSION=257.0.0
ENV CLOUD_SDK_VERSION=$CLOUD_SDK_VERSION

ARG BAZEL_VERSION=0.28.0

# Get GCloud SDK
# Inspired by https://github.com/GoogleCloudPlatform/cloud-sdk-docker/blob/master/debian/Dockerfile
RUN apt-get -qqy update && apt-get install -qqy \
        apt-transport-https \
        curl \
        gcc \
        git \
        gnupg \
        lsb-release \
        openssh-client \
        python-dev \
        python-pip \
        tzdata \
    && pip install -U crcmod   && \
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" > /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update && \
    apt-get install -y google-cloud-sdk=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-app-engine-python=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-app-engine-go=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-datastore-emulator=${CLOUD_SDK_VERSION}-0 \
    && gcloud config set core/disable_usage_reporting true \
    && gcloud config set component_manager/disable_update_check true \
    && gcloud config set metrics/environment true

# Bazel
RUN curl -O "https://storage.googleapis.com/bazel-apt/pool/jdk1.8/b/bazel/bazel_${BAZEL_VERSION}_amd64.deb" && \
    apt-get install --quiet --yes "./bazel_${BAZEL_VERSION}_amd64.deb" && \
    rm "bazel_${BAZEL_VERSION}_amd64.deb"

# Install AWS
RUN pip install awscli

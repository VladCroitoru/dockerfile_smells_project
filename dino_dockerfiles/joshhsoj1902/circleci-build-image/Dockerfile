FROM alpine:3.11

RUN mkdir -p /tmp/workspace \
 && mkdir -p /tmp/logs

RUN apk --no-cache add git curl make bash openssh sudo jq

ENV DOCKER_BUILDKIT=1

COPY --from=docker:19.03.11 /usr/local/bin/docker /bin/docker


# Gcloud https://github.com/GoogleCloudPlatform/cloud-sdk-docker/blob/master/alpine/Dockerfile
ENV CLOUD_SDK_VERSION 298.0.0
ENV CLOUDSDK_PYTHON=python3
ENV PATH /google-cloud-sdk/bin:$PATH
RUN apk --no-cache add \
        curl \
        python3 \
        py3-crcmod \
        bash \
        libc6-compat \
        openssh-client \
        git \
        gnupg \
    && curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    gcloud config set metrics/environment github_docker_image && \
    gcloud --version

# Docker-compose 
RUN apk add --no-cache gcc python-dev libffi-dev openssl-dev libc-dev make py-pip gcc
RUN pip install --trusted-host pypi.python.org docker-compose

RUN curl https://raw.githubusercontent.com/kadwanev/retry/master/retry -o /usr/local/bin/retry \
 && chmod +x /usr/local/bin/retry

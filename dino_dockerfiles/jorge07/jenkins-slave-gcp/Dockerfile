FROM jenkinsci/jnlp-slave:3.15-1

LABEL maintainer="Jorge Arco <jorge.arcoma@gmail.com>"

ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1
ENV PATH /opt/google-cloud-sdk/bin:$PATH
ENV DOCKER_API_VERSION=1.23
ENV DOCKER_COMPOSE_VERSION 1.12.0

USER root

# Install Google Cloud Components
RUN apt update \
    && apt install -y ant curl python python-pip gettext-base rsync \
    && curl https://sdk.cloud.google.com | bash \
    && mv google-cloud-sdk /opt \
    && gcloud components install kubectl \
    && curl -fsSL https://get.docker.com/ | sh \
    && pip install docker-compose


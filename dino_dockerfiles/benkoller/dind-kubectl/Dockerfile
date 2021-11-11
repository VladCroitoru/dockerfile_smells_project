FROM docker:17.06.2-ce

ENV KUBERNETES_VERSION v1.7.9
ENV DOCKER_COMPOSE_VERSION 1.18.0

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
    curl \
    bash \
    vim \
    jq \
    git \
    openssl-dev \
    libffi-dev \
  && rm -rf /var/cache/apk/*

RUN curl -o /usr/local/bin/kubectl "https://storage.googleapis.com/kubernetes-release/release/"$KUBERNETES_VERSION"/bin/linux/amd64/kubectl" && \
    chmod +x /usr/local/bin/kubectl


RUN pip install "docker-compose==$DOCKER_COMPOSE_VERSION"

ENTRYPOINT /bin/bash
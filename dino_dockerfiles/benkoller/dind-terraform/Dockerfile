FROM docker:17.06.2-ce

ENV TERRAFORM_VERSION 0.10.6
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
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

RUN curl -o /tmp/terraform.zip "https://releases.hashicorp.com/terraform/"$TERRAFORM_VERSION"/terraform_"$TERRAFORM_VERSION"_linux_amd64.zip" && \
    unzip /tmp/terraform.zip && \
    chmod +x terraform && \
    mv terraform /usr/local/bin

RUN pip install "docker-compose==$DOCKER_COMPOSE_VERSION"

ENTRYPOINT /bin/bash
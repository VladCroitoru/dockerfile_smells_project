ARG BASE_IMG=alpine:3.11.5
FROM golang:1.14.2-alpine3.11 as gobuilder

ARG GOOS=linux
ARG GOARCH=amd64
ARG CGO_ENABLED=0

RUN apk add --no-cache --update \
    bash \
    binutils \
    build-base \
    ca-certificates \
    curl

ENV TERRAGRUNT_VERSION=0.31.10
ENV TERRAGRUNT_DOWNLOAD_URL=https://github.com/gruntwork-io/terragrunt/releases/download
RUN curl -fsSL -O ${TERRAGRUNT_DOWNLOAD_URL}/v${TERRAGRUNT_VERSION}/terragrunt_linux_amd64 && \
    curl -fsSL ${TERRAGRUNT_DOWNLOAD_URL}/v${TERRAGRUNT_VERSION}/SHA256SUMS | grep terragrunt_linux_amd64 > SHA256SUMS && \
    sha256sum -c SHA256SUMS && \
    mv terragrunt_linux_amd64 /usr/local/bin/terragrunt

ENV TERRAFORM_VERSION=1.0.6
ENV TERRAFORM_RELEASE_URL=https://releases.hashicorp.com/terraform
RUN curl -fsSL -O ${TERRAFORM_RELEASE_URL}/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    curl -fsSL ${TERRAFORM_RELEASE_URL}/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS | grep terraform_${TERRAFORM_VERSION}_linux_amd64.zip > SHA256SUMS && \
    sha256sum -c SHA256SUMS && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    mv terraform /usr/local/bin/

ENV OPA_VERSION=0.32.0
WORKDIR /opa-build
RUN curl -fsSL "https://codeload.github.com/open-policy-agent/opa/tar.gz/v${OPA_VERSION}" | tar xvz --strip-components=1 && \
    go build && \
    mv opa /usr/local/bin/

ENV CONFTEST_VERSION=0.27.0
ENV CONFTEST_DOWNLOAD_URL=https://github.com/instrumenta/conftest/releases/download
RUN curl -fsSL -O ${CONFTEST_DOWNLOAD_URL}/v${CONFTEST_VERSION}/conftest_${CONFTEST_VERSION}_Linux_x86_64.tar.gz && \
    curl -fsSL ${CONFTEST_DOWNLOAD_URL}/v${CONFTEST_VERSION}/checksums.txt | grep conftest_${CONFTEST_VERSION}_Linux_x86_64.tar.gz > checksums.txt && \
    sha256sum -c checksums.txt && \
    tar xz conftest -C /usr/local/bin/ -f conftest_${CONFTEST_VERSION}_Linux_x86_64.tar.gz

RUN strip --strip-all /usr/local/bin/* && \
    chmod 0755 /usr/local/bin/*

FROM ${BASE_IMG}
LABEL maintainer="Rémi REY <rrey94@gmail.com>"

COPY --from=gobuilder /usr/local/bin/ /usr/bin/
COPY Gemfile .

RUN apk add --no-cache --update \
    ruby ruby-webrick ruby-etc ruby-io-console bash docker && \
    apk add --no-cache --update --virtual build-dependencies \
    build-base \
    ruby-dev && \
    gem install bundler && \
    bundle config set no-cache true && \
    bundle install --jobs $(getconf _NPROCESSORS_ONLN) && \
    apk del build-dependencies

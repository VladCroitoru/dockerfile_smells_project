FROM golang:alpine as gobuilder

RUN apk add git
ENV GO111MODULE=on
RUN go get github.com/hashicorp/terraform-config-inspect \
 && cp `which terraform-config-inspect` /

FROM alpine:latest

ENV TERRAFORM_VERSION=1.0.8
ENV TERRATEST_LOG_PARSER_VERSION=v0.32.9
ENV TERRAFORM_DOCS_VERSION=v0.11.2
ENV AWS_IAM_AUTHENTICATOR="1.15.10/2020-02-22"
ENV KUBECTL_VERSION=v1.19.8

ENV TF_BUILD_HARNESS_PATH=/tf-build-harness

# custom bin directory
RUN mkdir -p ${TF_BUILD_HARNESS_PATH}
ADD bin ${TF_BUILD_HARNESS_PATH}/bin
RUN chmod +x ${TF_BUILD_HARNESS_PATH}/bin/*
ENV PATH=${TF_BUILD_HARNESS_PATH}/bin:$PATH

# update/upgrade and all other packages
RUN apk update \
 && apk upgrade \
 && apk add curl gnupg go git unzip bash libssl1.1 libcrypto1.1 libffi-dev build-base linux-headers zlib-dev openssl-dev readline-dev openssh-client coreutils python3

# kubectl

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
 && chmod +x ./kubectl \
 && mv ./kubectl /usr/local/bin

# aws-iam-authenticator

RUN curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/${AWS_IAM_AUTHENTICATOR}/bin/linux/amd64/aws-iam-authenticator \
 && curl -o aws-iam-authenticator.sha256 https://amazon-eks.s3-us-west-2.amazonaws.com/${AWS_IAM_AUTHENTICATOR}/bin/linux/amd64/aws-iam-authenticator.sha256 \
 && sha256sum -c --ignore-missing aws-iam-authenticator.sha256 \
 && chmod +x ./aws-iam-authenticator \
 && mv aws-iam-authenticator /usr/local/bin

# terraform
ADD pgp_keys.asc .
RUN curl -Os https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
 && curl -Os https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS \
 && cat pgp_keys.asc | gpg --import \
 && curl -Os https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS.sig \
 && gpg --verify terraform_${TERRAFORM_VERSION}_SHA256SUMS.sig terraform_${TERRAFORM_VERSION}_SHA256SUMS \
 && sha256sum -c terraform_${TERRAFORM_VERSION}_SHA256SUMS 2>&1 | grep "${TERRAFORM_VERSION}_linux_amd64.zip:\sOK" \
 && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin \
 && rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip

# terraform-docs
RUN curl -OsL https://github.com/segmentio/terraform-docs/releases/download/${TERRAFORM_DOCS_VERSION}/terraform-docs-${TERRAFORM_DOCS_VERSION}-linux-amd64 \
 && mv terraform-docs-${TERRAFORM_DOCS_VERSION}-linux-amd64 /usr/local/bin/terraform-docs \
 && chmod +x /usr/local/bin/terraform-docs

# gopath
ENV GOPATH /workdir

# terratest_log_parser
RUN curl -Os \
 https://github.com/gruntwork-io/terratest/releases/download/${TERRATEST_LOG_PARSER_VERSION}/terratest_log_parser_linux_amd64 \
 && mv terratest_log_parser_linux_amd64 /usr/local/bin/terratest_log_parser \
 && chmod +x /usr/local/bin/terratest_log_parser

# terraform-config-inspect
COPY --from=gobuilder /terraform-config-inspect /usr/local/bin/terraform-config-inspect

WORKDIR /work

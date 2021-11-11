FROM alpine:3.7
LABEL maintainer "Kazuya Hara"

ENV AWSCIL_VERSION=1.14.44
ENV TERRAFORM_VERSION=0.11.3

RUN apk add -v --update python py-pip curl && \
    curl https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip > terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin && \
    rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    pip install awscli==${AWSCIL_VERSION} && \
    apk del -v --purge py-pip && \
    rm /var/cache/apk/*

COPY . .

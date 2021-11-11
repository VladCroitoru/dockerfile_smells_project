FROM python:3-alpine3.7
MAINTAINER Andrew Rowson <docker@growse.com>

ENV TERRAFORM_VERSION=0.11.3
RUN apk add --no-cache curl git

RUN apk add --update zip && \
    curl -sSL https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -o /tmp/terraform.zip && \
    unzip /tmp/terraform.zip -d /usr/bin && \
    rm /tmp/terraform.zip && \
    apk del zip && \
    rm -rf /var/cache/apk/*

CMD ["terraform"]


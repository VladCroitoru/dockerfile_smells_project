FROM alpine:3.6

LABEL maintainer="Stephen Steiner<ntwrkguru@gmail.com>"

## Install base packages
RUN apk add --no-cache python2-dev py2-pip build-base libffi-dev openssl-dev && \
    pip install --upgrade pip cffi && \
    pip install ansible

WORKDIR /playbook

VOLUME ["/playbook"]

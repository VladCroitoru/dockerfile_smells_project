FROM python:3-alpine3.11

# Python changed their image, this is for backwards compat
RUN ln -s /usr/local/bin/python /usr/bin/python

RUN set -xe \
    && apk add --no-cache \
        ansible \
        docker \
        tar \
        git \
        openssh-client \
        jq \
        curl \
    && pip install \
        awscli \
        boto \
        yamllint
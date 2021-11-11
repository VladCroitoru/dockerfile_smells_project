FROM node:8

LABEL maintainer="blockchain@intellecteu.com"

RUN apt-get update && apt-get install -y \
    python-dev zip jq \
    && curl -O https://bootstrap.pypa.io/get-pip.py \
    && python get-pip.py \
    && pip install awscli
    



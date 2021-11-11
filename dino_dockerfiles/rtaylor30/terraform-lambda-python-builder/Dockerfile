FROM ubuntu:16.04

LABEL maintainer=webframeworks@manheim.com
LABEL repo=manheimwebframework/terraform-lambda-python-builder

RUN apt update \
    && apt upgrade -q -y \
    && apt install -q -y python3 python3-pip curl unzip git make \
    && pip3 install --upgrade pip \
    && pip3 install awscli virtualenv Jinja2 \
    && curl -LO https://releases.hashicorp.com/terraform/0.9.6/terraform_0.9.6_linux_amd64.zip \
    && unzip terraform_0.9.6_linux_amd64.zip \
    && mv terraform /usr/bin/ \
    && chmod +x /usr/bin/terraform \
    && rm terraform_0.9.6_linux_amd64.zip

COPY requirements.txt /etc/requirements.txt
RUN pip3 install -r /etc/requirements.txt

WORKDIR /app
CMD sh build.sh


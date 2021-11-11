# Shamelessly pulled from @leftathome
FROM chef/chefdk:latest
MAINTAINER nick@nickmontgomery.com
ENTRYPOINT "/bin/sh"
ARG TF_VERSION=0.11.3
ARG TFLINT_VERSION=0.5.3
WORKDIR /tmp
ADD Gemfile .
RUN apt-get update && apt-get install -y unzip zip \
  git build-essential && apt-get clean && \
  chef exec bundle install && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN wget https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip && unzip terraform_${TF_VERSION}_linux_amd64.zip -d /usr/bin/ && rm terraform_*.zip; wget https://github.com/wata727/tflint/releases/download/v${TFLINT_VERSION}/tflint_linux_amd64.zip && unzip tflint_linux_amd64.zip && mv tflint /usr/local/bin/tflint && rm -f tflint_linux_amd64.zip; wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && rm get-pip.py
ENTRYPOINT /bin/bash

FROM python:3.4.6
MAINTAINER Luca Santarella, luca.santarella@gmail.com

# AWS CLI needs the PYTHONIOENCODING environment varialbe to handle UTF-8 correctly:
ENV PYTHONIOENCODING=UTF-8

# Install apt packages
RUN apt-get -y update && apt-get -y install \
    unzip \
    jq

# Install AWS Cli
RUN \ 
    curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"; \
    unzip awscli-bundle.zip; \
    ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws;

# Install docker client binaries
RUN curl -L -o /tmp/docker-17.03.0-ce.tgz https://get.docker.com/builds/Linux/x86_64/docker-17.03.0-ce.tgz; \
    tar -xz -C /tmp -f /tmp/docker-17.03.0-ce.tgz; \
    mv /tmp/docker/* /usr/bin;
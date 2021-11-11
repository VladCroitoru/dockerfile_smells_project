FROM ubuntu:14.04
MAINTAINER Robert Andersson <kemichal@gmail.com>

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    smbclient \
    python \
    curl \
    unzip \
    mysql-client

RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" && \
    unzip awscli-bundle.zip && \
    ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

RUN rm awscli-bundle.zip & \
    rm -r awscli-bundle

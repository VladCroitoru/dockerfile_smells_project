FROM garethjevans/jenkinsslave:v1.3-alpine

MAINTAINER Martin Ford <ford.j.martin@gmail.com>

ENV GCLOUD_SDK_VERSION=183.0.0
ENV GCLOUD_SDK_URL=https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${GCLOUD_SDK_VERSION}-linux-x86_64.tar.gz
ENV TERRAFORM_VERSION="0.11.3"
ENV PATH="${PATH}:/opt/google-cloud-sdk/bin"

RUN apk add --update \
      curl \
      python \
      python-dev && \
    rm -rf /var/cache/apk/*

RUN mkdir -p /opt && \
    cd /opt && \
    wget -q -O - $GCLOUD_SDK_URL |tar zxf - && \
    /opt/google-cloud-sdk/install.sh -q

RUN chown jenkins:jenkins -R /home/jenkins

RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    chmod +x terraform && \
    mv terraform /usr/bin/terraform && \
    rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip

USER jenkins
WORKDIR /home/jenkins

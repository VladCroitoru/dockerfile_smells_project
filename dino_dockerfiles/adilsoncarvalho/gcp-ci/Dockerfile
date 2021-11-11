FROM docker:17.06.0-ce-git

LABEL maintainer "Adilson Carvalho <lc.adilson@gmail.com>"

ENV CLOUDSDK_VERSION 161.0.0

# Common dependencies

RUN apk update && apk add curl py-pip

# Installing docker-compose

RUN pip install docker-compose

# Installing gcloud

RUN curl -o /tmp/google-cloud-sdk.tar.gz https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-$CLOUDSDK_VERSION-`uname -s`-`uname -m`.tar.gz \
    && tar -xvf /tmp/google-cloud-sdk.tar.gz -C / \
    && /google-cloud-sdk/install.sh -q \
    && source /google-cloud-sdk/path.bash.inc

ENV PATH ${PATH}:/google-cloud-sdk/bin

# Installing kubectl

RUN gcloud components install kubectl -q

# Installing our gcp-ci helper scripts

RUN mkdir -p /opt/gcp-ci
COPY ./gcp-ci /opt/gcp-ci
ENV PATH ${PATH}:/opt/gcp-ci

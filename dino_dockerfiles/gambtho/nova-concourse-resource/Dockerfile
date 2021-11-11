FROM openjdk:8-jre-alpine

ENV SBT_VERSION 0.13.8

RUN apk add --no-cache bash curl jq openrc git python python-dev py-pip build-base && \
    apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main --repository  http://dl-cdn.alpinelinux.org/alpine/edge/community docker

COPY ./scripts/check /opt/resource/check
COPY ./scripts/in /opt/resource/in
COPY ./scripts/out /opt/resource/out
COPY ./scripts/common.sh /opt/resource/common.sh

RUN chmod +x /opt/resource/out /opt/resource/in /opt/resource/check
RUN pip install gilt-nova
RUN pip install awscli
RUN git clone https://github.com/gilt/nova-shared-templates.git ~/.nova

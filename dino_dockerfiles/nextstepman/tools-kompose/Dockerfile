FROM ubuntu:xenial

ARG KOMPOSE_VERSION=v1.16.0
ARG KOMPOSE_URL=https://github.com/kubernetes/kompose/releases/download/${KOMPOSE_VERSION}/kompose-linux-amd64

ENV KOMPOSE_PATH /home/kompose

RUN apt-get update \
    && apt-get install -y wget \
    && wget -O kompose ${KOMPOSE_URL} \
    && chmod 755 kompose \
    && mv kompose /usr/local/bin \
    && mkdir -p $KOMPOSE_PATH/workdir \
    && adduser --home $KOMPOSE_PATH --disabled-password --gecos '' kompose \
    && chown -R kompose:kompose $KOMPOSE_PATH

USER kompose

WORKDIR $KOMPOSE_PATH/workdir

ENTRYPOINT ["kompose"]


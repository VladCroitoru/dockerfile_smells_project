FROM golang:1.7.3-alpine
MAINTAINER Serge Ovchinnikov <sovchinn@gmail.com>

ENV GAE_VER 1.9.46
ENV GAE_ZIP go_appengine_sdk_linux_amd64-$GAE_VER.zip

ENV GSDK_VER 133.0.0
ENV GSDK_ZIP google-cloud-sdk-$GSDK_VER-linux-x86_64.tar.gz

RUN apk --no-cache add \
      bash \
      git \
      py-pip \
      python &&\
    pip install --upgrade pip

ADD https://storage.googleapis.com/appengine-sdks/featured/$GAE_ZIP .
RUN unzip -q $GAE_ZIP -d /usr/local
RUN rm $GAE_ZIP

ADD https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/$GSDK_ZIP .
RUN tar -xvzf $GSDK_ZIP -C /usr/local/
RUN rm $GSDK_ZIP

ENV PATH $PATH:/usr/local/go_appengine/:/usr/local/google-cloud-sdk/bin/

VOLUME ["/gae_key"]

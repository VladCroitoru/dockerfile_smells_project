FROM alpine:3.8
MAINTAINER WIFIPLUG

RUN apk add --no-cache libc6-compat curl unzip ca-certificates
RUN mkdir /xray
WORKDIR /xray

RUN curl https://s3.dualstack.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-linux-3.x.zip -o install.zip
RUN unzip ./install.zip
RUN mv xray /usr/bin/xray

WORKDIR /xray

RUN rm -rf /xray
RUN apk del curl unzip

ENV BIND_ADDRESS="0.0.0.0"

ENTRYPOINT /usr/bin/xray -b $BIND_ADDRESS:2000
EXPOSE 2000/udp
FROM alpine:3.6

RUN apk add --no-cache libc6-compat curl unzip ca-certificates

RUN mkdir workspace

WORKDIR workspace

RUN curl https://s3.dualstack.us-east-1.amazonaws.com/aws-xray-assets.us-east-1/xray-daemon/aws-xray-daemon-linux-2.x.zip -o install.zip
RUN unzip ./install.zip
RUN mv xray /usr/bin/xray

WORKDIR /

RUN rm -rf workspace
RUN apk del curl unzip

EXPOSE 2000/udp

ENTRYPOINT ["xray"]

CMD ["--bind=0.0.0.0:2000", "--region=eu-west-1"]

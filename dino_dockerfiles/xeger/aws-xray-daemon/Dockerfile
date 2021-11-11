FROM debian:stable-slim
EXPOSE 2000/udp
ENV AWS_ACCESS_KEY_ID=
ENV AWS_REGION=
ENV AWS_SECRET_ACCESS_KEY=

WORKDIR /srv
CMD ["/srv/xray"]

ADD https://s3.amazonaws.com/aws-xray-assets.us-east-1/xray-daemon/aws-xray-daemon-linux-1.x.zip /tmp
RUN apt-get update && apt-get install -y ca-certificates openssl unzip && unzip /tmp/aws-xray-daemon-linux-1.x.zip && apt-get remove -y unzip && apt-get clean
ADD cfg.yaml /srv/cfg.yaml

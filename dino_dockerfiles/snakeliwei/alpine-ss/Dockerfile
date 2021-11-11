FROM alpine
MAINTAINER Lyndon li <snakeliwei@gmail.com>
RUN apk add --update py-pip && rm -rf /var/cache/apk/*
RUN pip install shadowsocks==2.8.2

# Configure container to run as an executable
ENTRYPOINT ["/usr/bin/ssserver"]

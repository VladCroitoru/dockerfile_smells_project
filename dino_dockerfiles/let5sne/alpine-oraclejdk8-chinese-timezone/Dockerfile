# Builds a minimal docker image with oraclejdk 

FROM frolvlad/alpine-oraclejdk8
MAINTAINER let5sne <let5sne@gmail.com>

RUN apk update && apk add ca-certificates && \
    apk add tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone

FROM alpine:3.5

MAINTAINER Zack Shahan "z.shahan@gmail.com"

ENV uid 1001

RUN apk add --no-cache \
        git \
        unzip \
        bash \
        openssh \
        openssl \
        jq \
        curl \
        wget
        
USER $uid

CMD ["git", "--version"]

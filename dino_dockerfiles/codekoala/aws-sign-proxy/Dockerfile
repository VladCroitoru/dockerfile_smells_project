FROM alpine:3.7
MAINTAINER Josh VanderLinden <codekoala@gmail.com>

RUN apk update && \
    apk add ca-certificates

ADD ./bin/aws-sign-proxy /bin/

ENTRYPOINT /bin/aws-sign-proxy

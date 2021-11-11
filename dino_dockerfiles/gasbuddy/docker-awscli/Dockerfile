FROM alpine:latest

RUN addgroup awscli-app && adduser -SDHG awscli-app awscli-app

RUN apk --no-cache add py-pip python &&\
    pip install --upgrade pip awscli &&\
    apk add --update curl &&\
    apk del py-pip

USER awscli-app

VOLUME ["/data"]

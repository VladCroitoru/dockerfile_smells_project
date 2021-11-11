FROM golang:alpine AS builder

ENV WEBHOOK_VERSION 2.6.8
ENV SRC_PATH $GOPATH/src/github.com/adnanh

RUN apk add --update -t build-deps curl go git libc-dev gcc libgcc \
    && curl -L -o /tmp/webhook-${WEBHOOK_VERSION}.tar.gz https://github.com/adnanh/webhook/archive/${WEBHOOK_VERSION}.tar.gz \
    &&  mkdir -p ${SRC_PATH} && tar -xvzf /tmp/webhook-${WEBHOOK_VERSION}.tar.gz -C ${SRC_PATH} \
    && mv -f ${SRC_PATH}/webhook-* ${SRC_PATH}/webhook \
    && cd ${SRC_PATH}/webhook && go get -d && go build -o /usr/local/bin/webhook


FROM docker:stable
ENV WEBHOOK_VERSION 2.6.8

RUN apk add --no-cache git openssh-client curl bash

COPY --from=builder /usr/local/bin/webhook /usr/local/bin/webhook
COPY config/ /var/webhook/
EXPOSE      9000

VOLUME [ "/var/webhook" ]
ENTRYPOINT  ["/usr/local/bin/webhook"]

CMD [ "-hooks", "/var/webhook/hooks.json", "-verbose", "-hotreload"]
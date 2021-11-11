FROM golang:1.8-alpine as builder

RUN apk --update add git;
RUN go get -d github.com/optiopay/klar
RUN go build ./src/github.com/optiopay/klar

FROM node:8-alpine

RUN apk -Uuv add --no-cache curl ca-certificates && \
    apk add python3 && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    pip3 install awscli --upgrade && \
    rm -r /usr/lib/python*/ensurepip && \
    rm -r /root/.cache && \
    rm -rf /var/cache/apk/*
COPY --from=builder /go/klar /klar

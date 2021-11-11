FROM golang:alpine as vert
RUN apk --no-cache add git
ENV GOPATH /go
RUN go get -u github.com/Masterminds/vert

FROM golang:alpine as jfrog
RUN apk --no-cache add git
ENV GOPATH /go
RUN GOOS=linux go get -u github.com/jfrogdev/jfrog-cli-go/jfrog-cli/jfrog

FROM alpine:latest
RUN apk --no-cache add ca-certificates git bash jq
COPY --from=vert /go/bin/vert /usr/local/bin/vert
COPY --from=jfrog /go/bin/jfrog /usr/local/bin/jfrog
COPY --from=mikefarah/yq /usr/bin/yq /usr/local/bin/yq

ENV JFROG_CLI_LOG_LEVEL ERROR
ENV JFROG_CLI_OFFER_CONFIG false

RUN apk --no-cache add openssl

ADD assets/ /opt/resource/

RUN chmod +x /opt/resource/*
RUN mkdir /opt/resource/logs/
RUN mkdir v1.0
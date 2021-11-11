##############################################################
## Stage 1 - Go Build
##############################################################

FROM golang:1.16.9-alpine AS builder

RUN apk add --no-cache build-base

ADD . /go/src/github.com/cloud-barista/cb-ladybug

WORKDIR /go/src/github.com/cloud-barista/cb-ladybug

#RUN go build -mod=mod -ldflags '-w -extldflags "-static"' -tags cb-ladybug -o cb-ladybug -v
RUN make

#############################################################
## Stage 2 - Application Setup
##############################################################

FROM ubuntu:latest AS prod

# use bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

WORKDIR /app/src

COPY --from=builder /go/src/github.com/cloud-barista/cb-ladybug/conf/ /app/conf/

COPY --from=builder /go/src/github.com/cloud-barista/cb-ladybug/cmd/cb-ladybug /app/cmd/

#RUN /bin/bash -c "source /app/conf/setup.env"
ENV CBSTORE_ROOT /app
ENV CBLOG_ROOT /app
ENV APP_ROOT /app

ENV LISTEN_ADDRESS :1592
ENV BASE_PATH /ladybug

ENV SPIDER_CALL_METHOD REST
ENV TUMBLEBUG_CALL_METHOD REST
ENV MCKS_CALL_METHOD REST
ENV SPIDER_URL http://cb-spider:1024/spider
ENV TUMBLEBUG_URL http://cb-tumblebug:1323/tumblebug
ENV MCKS_URL http://cb-mcks:1470/mcks

ENV API_USERNAME default
ENV API_PASSWORD default

# Environment variables that you don't need to touch

# Ignore a protocol buffer namespace conflict 
ENV GOLANG_PROTOBUF_REGISTRATION_CONFLICT ignore

# Swagger UI API document file path 
#ENV API_DOC_PATH /app/api/rest/docs/swagger.json

ENTRYPOINT [ "/app/cmd/cb-ladybug" ]

EXPOSE 1592

FROM golang:1.12-alpine as build

RUN apk update

RUN apk add git ca-certificates

ADD . /go/src/github.com/racerxdl/mqtttelegram

WORKDIR /go/src/github.com/racerxdl/mqtttelegram

RUN GO111MODULE=on CGO_ENABLED=0 go get -v

RUN GO111MODULE=on CGO_ENABLED=0 GOOS=linux go build -o mqtttelegram


FROM alpine:latest
MAINTAINER Lucas Teske <lucas@teske.com.br>

RUN apk --no-cache add ca-certificates
RUN mkdir -p /opt/mqtttelegram
WORKDIR /opt/mqtttelegram

COPY --from=build /go/src/github.com/racerxdl/mqtttelegram/mqtttelegram .

ENV mqtt_server "mosquitto.mosquitto"
ENV mqtt_topic "ircredirect"

CMD /opt/mqtttelegram/mqtttelegram

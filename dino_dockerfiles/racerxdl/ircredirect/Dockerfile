FROM golang:1.12-alpine as build

RUN apk update

RUN apk add git ca-certificates

ADD . /go/src/github.com/racerxdl/ircredirect

WORKDIR /go/src/github.com/racerxdl/ircredirect

RUN GO111MODULE=on CGO_ENABLED=0 go get -v

RUN GO111MODULE=on CGO_ENABLED=0 GOOS=linux go build -o ircredirect


FROM alpine:latest
MAINTAINER Lucas Teske <lucas@teske.com.br>

RUN apk --no-cache add ca-certificates
RUN mkdir -p /opt/ircredirect
WORKDIR /opt/ircredirect

COPY --from=build /go/src/github.com/racerxdl/ircredirect/ircredirect .

ENV irc_server "irc.freenode.com"
ENV irc_channel "#ircredirect"
ENV mqtt_server "mosquitto.mosquitto"
ENV mqtt_topic "ircredirect"

CMD /opt/ircredirect/ircredirect

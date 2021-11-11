ARG BUILDPLATFORM="linux/amd64"
FROM --platform=$BUILDPLATFORM golang:1.16-alpine as build

ARG TARGETPLATFORM
ARG BUILDPLATFORM

RUN apk add --no-cache git

COPY ./ /go/src/github.com/itfactory-tm/thomas-bot

WORKDIR /go/src/github.com/itfactory-tm/thomas-bot

RUN export GOARM=6 && \
    export GOARCH=amd64 && \
    if [ "$TARGETPLATFORM" == "linux/arm64" ]; then export GOARCH=arm64; fi && \
    if [ "$TARGETPLATFORM" == "linux/arm" ]; then export GOARCH=arm; fi && \
    go build -ldflags "-X main.revision=$(git rev-parse --short HEAD)" ./cmd/thomas/

FROM alpine:3.13

RUN apk add --no-cache ca-certificates

RUN mkdir -p /go/src/github.com/itfactory-tm/thomas-bot/thomas-bot
WORKDIR /go/src/github.com/itfactory-tm/thomas-bot/thomas-bot
COPY ./sounds /go/src/github.com/itfactory-tm/thomas-bot/thomas-bot/sounds
COPY ./www /go/src/github.com/itfactory-tm/thomas-bot/thomas-bot/www
COPY ./config.json /go/src/github.com/itfactory-tm/thomas-bot/thomas-bot/

COPY --from=build /go/src/github.com/itfactory-tm/thomas-bot/thomas /usr/local/bin/

CMD [ "/usr/local/bin/thomas", "serve" ]

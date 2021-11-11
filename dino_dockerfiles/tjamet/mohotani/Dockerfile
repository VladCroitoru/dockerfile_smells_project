FROM golang:1.9.2-alpine as build

RUN apk add --no-cache git

COPY ./vendor /go/src/github.com/tjamet/mohotani/vendor
COPY ./cli /go/src/github.com/tjamet/mohotani/cli
COPY ./dns /go/src/github.com/tjamet/mohotani/dns
COPY ./ip /go/src/github.com/tjamet/mohotani/ip
COPY ./listener /go/src/github.com/tjamet/mohotani/listener
COPY ./logger /go/src/github.com/tjamet/mohotani/logger

RUN go build -o /bin/mohotani github.com/tjamet/mohotani/cli/mohotani

# cannot run the race detecrot on alpine: https://github.com/golang/go/issues/14481
RUN go list github.com/tjamet/mohotani/... | grep -v vendor | xargs go test -v


FROM alpine
RUN apk add --no-cache ca-certificates
COPY --from=build /bin/mohotani /bin/mohotani
ENTRYPOINT ["/bin/mohotani"]


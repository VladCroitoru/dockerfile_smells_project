### Gonk Dockerfile ###

################################
## Build Stage ##

FROM golang:1.15 as builder
WORKDIR /gonk
COPY . /gonk

## Build binary
RUN CGO_ENABLED=0 go build -a -o gonk cmd/gonk.go

################################
## Cert Stage ##

## Get CA certs 
FROM alpine:latest as certs
RUN apk --update add ca-certificates


################################
## Run Stage ##

FROM scratch 
## We need the certs because Scratch doesn't have them
COPY --from=certs /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

## Use binary from previous stage - multi-stage builds are awesome
COPY --from=builder /gonk/gonk /

ENV TOKEN $TOKEN
ENV GUILD_ID $GUILD_ID
ENV STREAM_CHANNEL $STREAM_CHANNEL

## Go Gonk Go!
CMD ["/gonk"]


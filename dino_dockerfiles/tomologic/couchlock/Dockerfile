FROM golang:1.9-alpine as builder
WORKDIR /go/src/couchlock
RUN apk --no-cache add git
COPY *.go ./
RUN go build -v

FROM alpine:3.6
RUN apk --no-cache add ca-certificates
COPY --from=builder /go/src/couchlock/couchlock /usr/bin/

ENTRYPOINT ["couchlock"]

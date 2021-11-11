FROM golang:1.10.3-alpine AS builder
MAINTAINER <nabeken@tknetworks.org>

ENV REPO=github.com/nabeken/go-api-now

RUN apk add --no-cache --update git

COPY . src/$REPO
WORKDIR /go/src/$REPO

RUN go get -d -v ./...
RUN go install -v

FROM alpine:3.8
MAINTAINER <nabeken@tknetworks.org>

RUN apk add --no-cache \
        ca-certificates

COPY --from=builder /go/bin/go-api-now /usr/local/bin
ENV GIN_MODE=release
EXPOSE 8000
USER nobody
CMD ["go-api-now"]

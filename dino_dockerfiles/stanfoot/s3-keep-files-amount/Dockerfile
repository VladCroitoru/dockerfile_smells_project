###############################
# Builder container
###############################

FROM golang:1.9.3 as builder
MAINTAINER Shota Sawada <sawada@stanfoot.com>

WORKDIR /go/src/github.com/stanfoot/s3-keep-files-amount
COPY . .

RUN go-wrapper download
RUN go-wrapper install
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /go/bin/s3-keep-files-amount .


###############################
# Exec container
###############################

From alpine:latest
COPY --from=builder /go/bin/s3-keep-files-amount /usr/bin/s3-keep-files-amount
RUN apk add --no-cache ca-certificates

CMD ['s3-keep-files-amount']
# SkyDNS: build
#
# docker build -t="bioshrek/skydns" .

FROM golang:1.3.3
MAINTAINER Huan Wang <shrekwang1@gmail.com>

# build skydns
RUN mkdir -p /go/src/github.com/skynetservices/skydns
RUN git clone https://github.com/skynetservices/skydns.git /go/src/github.com/skynetservices/skydns
RUN go get github.com/skynetservices/skydns
WORKDIR /go/src/github.com/skynetservices/skydns
RUN pwd
RUN go build -v

# export skydns
RUN mkdir -p /skydns-binaries
RUN cp skydns /skydns-binaries/
VOLUME /skydns-binaries


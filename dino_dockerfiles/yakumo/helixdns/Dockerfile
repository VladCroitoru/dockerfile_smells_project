# source
FROM ubuntu:14.04

MAINTAINER yakumo

RUN apt-get update
RUN apt-get install -qy git make
RUN apt-get install -qy software-properties-common
RUN add-apt-repository ppa:evarlast/golang1.4
RUN apt-get update
RUN apt-get install -qy golang-go

RUN mkdir -p /usr/local/go/bin
ENV GOPATH /usr/local/go
ENV GOBIN /usr/local/go/bin
ENV PATH $PATH:$GOBIN

RUN go get github.com/mrwilson/helixdns
RUN go install github.com/mrwilson/helixdns

EXPOSE 53

ENTRYPOINT ["helixdns", "-port", "53", "-forward", "8.8.8.8:53"]
CMD []

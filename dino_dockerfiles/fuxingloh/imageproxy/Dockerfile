FROM google/golang
MAINTAINER Sevki <s@sevki.org>

ADD . /go/src/willnorris.com/go/imageproxy
RUN go get willnorris.com/go/imageproxy/cmd/imageproxy

ENTRYPOINT ["/go/bin/imageproxy"]
CMD ["-addr", "0.0.0.0:8080"]

EXPOSE 8080

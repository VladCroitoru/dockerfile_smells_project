FROM golang:1.8

ENV PROJECT $GOPATH/src/github.com/fanach/dctl
WORKDIR $PROJECT

COPY . $PROJECT

RUN	go test $(go list ./... | grep -v /vendor/) && \
	go build -o dctl

VOLUME /var/run

CMD ["./dctl"]

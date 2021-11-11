FROM golang:1.5

RUN go get github.com/jacobmarshall/go-azure-slack && \
    go install github.com/jacobmarshall/go-azure-slack

ENTRYPOINT /go/bin/go-azure-slack
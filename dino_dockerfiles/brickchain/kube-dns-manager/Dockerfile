FROM golang:1.8

ADD . /go/src/github.com/brickchain/kube-dns-manager
WORKDIR /go/src/github.com/brickchain/kube-dns-manager

RUN GOARCH=amd64 GOOS=linux CGO_ENABLED=0 go build -tags netgo -ldflags '-extldflags "-static"' -o /kube-dns-manager .

FROM alpine:3.4
RUN apk --no-cache add ca-certificates
COPY --from=0 /kube-dns-manager /kube-dns-manager
ENTRYPOINT ["/kube-dns-manager"]
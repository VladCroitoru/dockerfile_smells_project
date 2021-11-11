FROM golang:1.8
WORKDIR /go/src/github.com/cego/docker-registry-pruner
COPY . /go/src/github.com/cego/docker-registry-pruner
RUN go get . && CGO_ENABLED=0 go build -a .

FROM scratch
ENTRYPOINT ["/docker-registry-pruner"]
COPY --from=0 /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=0 /go/src/github.com/cego/docker-registry-pruner/docker-registry-pruner /docker-registry-pruner

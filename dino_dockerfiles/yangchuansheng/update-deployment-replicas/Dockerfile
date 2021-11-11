FROM golang:alpine as builder

WORKDIR /go/src/update-deployment-replicas

RUN apk update && apk add git; \
    go get github.com/golang/dep/cmd/dep; \
    /go/bin/dep init && rm -rf Gopkg.toml; 
# RUN go get github.com/golang/dep/cmd/dep
# RUN /go/bin/dep init && rm -rf Gopkg.toml
COPY Gopkg.toml /go/src/update-deployment-replicas/
COPY main.go .
RUN /go/bin/dep ensure; \
    go build -o update-deployment-replicas ./main.go

From alpine:latest

WORKDIR /root/

COPY --from=builder /go/src/update-deployment-replicas/update-deployment-replicas .

RUN chmod +x /root/update-deployment-replicas

ENTRYPOINT ["/root/update-deployment-replicas"]

FROM golang:1.9 AS builder

WORKDIR /go/src/github.com/boivie/undergang
RUN go get -u github.com/golang/dep/cmd/dep
COPY Gopkg.lock Gopkg.toml /go/src/github.com/boivie/undergang/
RUN dep ensure -v -vendor-only

COPY main.go /go/src/github.com/boivie/undergang/
COPY app  /go/src/github.com/boivie/undergang/app

ARG UNDERGANG_VERSION=latest
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags "-X main.version=${UNDERGANG_VERSION}" .

FROM alpine:latest

RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /go/src/github.com/boivie/undergang/undergang .

VOLUME ["/config"]
CMD ["/root/undergang"]

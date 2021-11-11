FROM golang:1.9.2-alpine3.7 as builder
RUN apk --no-cache add make git
RUN mkdir -p /go/src/github.com/donachys/kubevalonline/
COPY . /go/src/github.com/donachys/kubevalonline/
WORKDIR /go/src/github.com/donachys/kubevalonline/
RUN make linux

FROM alpine:latest
RUN apk --no-cache add ca-certificates
COPY --from=builder /go/src/github.com/donachys/kubevalonline/bin/linux/amd64/kubevalonline .
COPY --from=builder /go/src/github.com/donachys/kubevalonline/app /root/go/src/github.com/donachys/kubevalonline/app
ENTRYPOINT ["/kubevalonline"]
EXPOSE 5000

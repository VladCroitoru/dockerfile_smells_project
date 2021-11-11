FROM golang:latest AS base

WORKDIR /go/src/github.com/z0r1k/whoamI
COPY . .

RUN go get github.com/golang/dep/cmd/dep
RUN dep ensure
RUN go vet .
RUN GOOS=linux GOARCH=386 CGO_ENABLED=0  go build -a --installsuffix cgo -ldflags="-s -w" -o whoamI .

FROM alpine:latest

RUN mkdir -p /opt/release
COPY --from=base /go/src/github.com/z0r1k/whoamI/whoamI /opt/release/whoamI

ENTRYPOINT ["/opt/release/whoamI"]
EXPOSE 80

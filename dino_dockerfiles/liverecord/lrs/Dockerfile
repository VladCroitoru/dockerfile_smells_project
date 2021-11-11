# LiveRecord GoLang application

# Build app
FROM golang:1.11 as builder
LABEL maintainer = "philipp@zoonman.com"

COPY . /go/src/app

RUN cd /go/src/app && \
    GO111MODULE=on CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -o /go/bin/lrs cmd/lrs/main.go

# Pack app
FROM scratch
LABEL maintainer = "philipp@zoonman.com"
COPY --from=builder /go/bin/lrs /go/bin/lrs
ENTRYPOINT ["/go/bin/lrs"]
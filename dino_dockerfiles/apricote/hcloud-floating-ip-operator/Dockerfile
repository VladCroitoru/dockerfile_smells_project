FROM golang:1.10-alpine AS builder
RUN apk --no-cache add curl git

RUN curl -fsSL -o /usr/local/bin/dep https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 && chmod +x /usr/local/bin/dep

RUN mkdir -p /go/src/github.com/apricote/hcloud-floating-ip-operator
WORKDIR /go/src/github.com/apricote/hcloud-floating-ip-operator

COPY Gopkg.toml Gopkg.lock ./
# copies the Gopkg.toml and Gopkg.lock to WORKDIR

RUN dep ensure -vendor-only
# install the dependencies without checking for go code

COPY ./ ./
# copies application code

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM alpine:latest  
RUN apk --no-cache add ca-certificates

WORKDIR /root/
COPY --from=builder /go/src/github.com/apricote/hcloud-floating-ip-operator .
CMD ["./app"]
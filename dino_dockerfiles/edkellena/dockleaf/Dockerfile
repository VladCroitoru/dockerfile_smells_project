FROM golang:1.9.2-stretch as builder

RUN curl -fsSL -o /usr/local/bin/dep https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-amd64 && chmod +x /usr/local/bin/dep

RUN mkdir -p /go/src/github.com/dockleaf/dockleaf
WORKDIR /go/src/github.com/dockleaf/dockleaf

COPY Gopkg.toml Gopkg.lock ./
RUN dep ensure -vendor-only

ADD dockleaf.go .

RUN CGO_ENABLED=0 GOOS=linux go build -a -buildmode=exe -installsuffix cgo -ldflags '-s' -o dockleaf .


FROM golang:1.9.2-alpine
# FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /app
COPY --from=builder /go/src/github.com/dockleaf/dockleaf /app/
ENTRYPOINT ./dockleaf

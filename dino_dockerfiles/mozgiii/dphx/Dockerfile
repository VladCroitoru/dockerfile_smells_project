FROM golang:1.16.1 as builder
RUN mkdir -p /go/src/github.com/MOZGIII/dphx
WORKDIR /go/src/github.com/MOZGIII/dphx
COPY . .
RUN CGO_ENABLED=0 go build -a -ldflags '-s -extldflags "-static"' ./cmd/dphx

FROM scratch
COPY --from=builder /go/src/github.com/MOZGIII/dphx/dphx /usr/local/bin/dphx
CMD ["/usr/local/bin/dphx"]
EXPOSE 1080

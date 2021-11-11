# Build
FROM golang as builder
WORKDIR /go/src/github.com/upsub/dispatcher
ADD . .
RUN go get github.com/mitchellh/gox
RUN env CGO_ENABLED=0 gox -ldflags="-s -w" -osarch="linux/amd64" -output ./bin/dispatcher

# Runtime
FROM alpine
COPY --from=builder /go/src/github.com/upsub/dispatcher/bin/dispatcher /upsub/dispatcher
WORKDIR /upsub
EXPOSE 4400
CMD ["./dispatcher"]

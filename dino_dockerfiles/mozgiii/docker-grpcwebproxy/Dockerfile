from golang:alpine as builder
RUN apk --no-cache add git
RUN go get -u github.com/improbable-eng/grpc-web/go/grpcwebproxy

from alpine
RUN apk --no-cache add ca-certificates
WORKDIR /
COPY --from=builder /go/bin/grpcwebproxy .
CMD ["/grpcwebproxy"]

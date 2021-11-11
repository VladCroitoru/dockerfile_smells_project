# builder layer
FROM golang:1.9-alpine as builder
COPY . /go/src/github.com/xjewer/snitch
RUN go build -o /snitch github.com/xjewer/snitch/cmd/snitch

# original image
FROM alpine:3.6
LABEL maintainer="xjewer@gmail.com"
RUN apk --update add ca-certificates
COPY --from=builder /snitch .
ENTRYPOINT ["/snitch"]
CMD ["--help"]

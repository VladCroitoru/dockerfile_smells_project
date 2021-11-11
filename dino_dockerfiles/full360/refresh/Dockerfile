FROM golang:1.9-alpine as builder

WORKDIR /go/src/github.com/full360/refresh/
RUN apk --no-cache add make
COPY . .
RUN make release

FROM alpine:latest

RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /go/src/github.com/full360/refresh/bin/linux/refresh .

CMD ["./refresh"]

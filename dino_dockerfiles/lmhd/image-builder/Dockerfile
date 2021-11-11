FROM golang:1.10 as builder
Add . /go/src/github.com/adampointer/image-builder
WORKDIR /go/src/github.com/adampointer/image-builder/
RUN go get
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM alpine:latest
RUN apk --no-cache add ca-certificates curl
WORKDIR /root/
COPY --from=builder /go/src/github.com/adampointer/image-builder/app .
ENTRYPOINT ["./app"]

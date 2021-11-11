FROM golang:1.10-alpine as builder
WORKDIR /go/src/oisann.net/
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

FROM alpine:latest
RUN apk --update add git openssh && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*
WORKDIR /root/
COPY --from=builder /go/src/oisann.net/main .
CMD ["./main"]

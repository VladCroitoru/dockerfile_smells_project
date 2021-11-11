FROM golang:1.10.0-alpine AS builder
WORKDIR /go/src/insane/kjob
COPY main.go .
RUN apk add -U git
RUN go get ./...
RUN CGO_ENABLED=0 go build -o kjob

FROM scratch
ADD rootfs /
COPY --from=builder /go/src/insane/kjob/kjob .
ENTRYPOINT ["/kjob"]
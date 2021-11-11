FROM golang:1.15.6-alpine AS builder
WORKDIR /go/src/github.com/snarlysodboxer/inplace-image-tag-updater
COPY go.mod ./
RUN go mod download
COPY . .
RUN GOOS=linux go build -o /inplace-image-tag-updater

FROM alpine:3.12 AS app
RUN apk add --no-cache curl git openssl wget bash
WORKDIR /code
COPY --from=builder /inplace-image-tag-updater /inplace-image-tag-updater
ENTRYPOINT ["/inplace-image-tag-updater"]

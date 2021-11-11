FROM golang:1.16-alpine AS build
RUN apk add --no-cache curl git build-base
WORKDIR $GOPATH/src/github.com/plgd-dev/sdk
COPY go.mod go.sum ./
RUN go mod download
COPY . .
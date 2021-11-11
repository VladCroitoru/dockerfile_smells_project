FROM golang:1.16.7-alpine3.13 AS build
WORKDIR /workspace
COPY go.mod .
COPY go.sum .
RUN go mod download
COPY *.go .
RUN CGO_ENABLED=0 go build -o zjchatserver .

FROM alpine:3.13.6
LABEL maintainer="Zhengjun HUO"
COPY --from=build /workspace/zjchatserver /zjchatserver
WORKDIR /
COPY zjunx.cfg /etc/zjunx/zjunx.cfg
COPY ssl/ /ssl/
ENTRYPOINT ["/zjchatserver"]

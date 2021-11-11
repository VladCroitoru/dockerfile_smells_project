FROM golang:alpine

WORKDIR /go/src/wenku
COPY . .

RUN go generate && go env && go build -o server .

FROM alpine:latest
LABEL MAINTAINER="SliverHorn@sliver_horn@qq.com"

WORKDIR /go/src/wenku

COPY --from=0 /go/src/wenku ./

EXPOSE 8888

ENTRYPOINT ./server -c config.docker.yaml

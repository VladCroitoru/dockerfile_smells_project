FROM golang:1.6
MAINTAINER  Elliott Rezny <erezny@gmail.com>

RUN mkdir -p /go/src/app
WORKDIR /go/src/app

COPY . /go/src/app
RUN go-wrapper download
RUN go-wrapper install

ENV URI elasticsearch:9200
ENV ALL true
ENV TIMEOUT 500ms
ENV LISTENADDRESS :9100
ENV LISTENPATH /metrics

EXPOSE      9100

CMD go-wrapper run --es.uri=${URI} --es.all=${ALL} --es.timeout=${TIMEOUT} --web.listen-address=${LISTENADDRESS} --web.telemetry-path=${LISTENPATH}

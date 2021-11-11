FROM golang:1.6-alpine

RUN mkdir -p /go/src/mandrill-prometheus-exporter
WORKDIR /go/src/mandrill-prometheus-exporter

RUN apk add --update git \
    && rm -rf /var/cache/apk/*

COPY . /go/src/mandrill-prometheus-exporter
RUN go get -v \
    && go install \
    && rm -rf /go/src/mandrill-prometheus-exporter \
    && mkdir -p /go/src/mandrill-prometheus-exporter

ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 9153
ENTRYPOINT ["mandrill-prometheus-exporter"]

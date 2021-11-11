FROM golang:alpine

RUN mkdir -p /go/src/nats_exporter
WORKDIR /go/src/nats_exporter

COPY . /go/src/nats_exporter

RUN apk add --no-cache --virtual .git git ; go-wrapper download ; apk del .git
RUN go-wrapper install

EXPOSE 9148
USER nobody
ENTRYPOINT ["nats_exporter"]

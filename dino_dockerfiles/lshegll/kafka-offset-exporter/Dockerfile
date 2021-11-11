FROM golang:alpine as builder
RUN apk --no-cache --virtual=build-dependencies add git make gcc g++ && \
    go get -v github.com/lshegll/kafka-offset-exporter
WORKDIR /go/src/github.com/lshegll/kafka-offset-exporter
RUN GOARCH=amd64 GOOS=linux go build -v -a -ldflags '-extldflags "-static" -s -w' -o /bin/kafka_exporter .

FROM alpine:3.6
COPY --from=builder /bin/kafka_exporter /bin/kafka_exporter
CMD ["/bin/sh", "-c", "/bin/kafka_exporter --log.level=\"debug\" --log.format=\"logger:stdout?json=true\" --kafka.server=\"${KAFKA_BROKERS}\" --web.telemetry-path=\"/metrics\" --web.listen-address=\":7979\" --topic.filter=\"${TOPIC_FILTER}\" --group.filter=\"${GROUP_FILTER}\" "]

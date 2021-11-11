FROM alpine:3.10

RUN apk add ca-certificates && update-ca-certificates

COPY fluentd-kinesis-forwarder-monitor /bin/fluentd-kinesis-forwarder-monitor

ENTRYPOINT ["/bin/fluentd-kinesis-forwarder-monitor"]

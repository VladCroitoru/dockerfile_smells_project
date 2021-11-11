FROM golang:1.4

ADD . /go/src/github.com/jmcarbo/consul-alerts
RUN go get github.com/jmcarbo/consul-alerts/...
RUN go install github.com/jmcarbo/consul-alerts

EXPOSE 9000

ENTRYPOINT [ "/go/bin/consul-alerts", "--alert-addr=0.0.0.0:9000" ]
CMD []

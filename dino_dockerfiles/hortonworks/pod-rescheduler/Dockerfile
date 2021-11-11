FROM golang:1.9.0

COPY . /go/src/github.com/hortonworks/pod-rescheduler
RUN cd /go/src/github.com/hortonworks/pod-rescheduler && make build-linux
RUN mv /go/src/github.com/hortonworks/pod-rescheduler/build/Linux/pod-rescheduler /

ENTRYPOINT ["/pod-rescheduler"]
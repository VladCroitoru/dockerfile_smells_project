FROM golang:1.8

ADD . /go/src/github.com/deviceio/agent

RUN cd /go/src/github.com/deviceio/agent
RUN go install github.com/deviceio/agent/cmd/deviceio-agent
RUN mkdir -p /etc/deviceio/agent && echo "{}" > /etc/deviceio/agent/config.json

ENTRYPOINT ["deviceio-agent"]
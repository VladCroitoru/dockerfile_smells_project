FROM golang:latest

ADD . /go/src/github.com/miton18/torque2warp10

RUN go install github.com/miton18/torque2warp10

EXPOSE 8080

ENTRYPOINT /go/bin/torque2warp10

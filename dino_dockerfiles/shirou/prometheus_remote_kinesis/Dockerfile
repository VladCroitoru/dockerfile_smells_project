### build stage
FROM golang:alpine AS build-env

RUN apk add --no-cache git
ADD . /go/src/github.com/shirou/prometheus_remote_kinesis
WORKDIR /go/src/github.com/shirou/prometheus_remote_kinesis
RUN go get -u

RUN CGO_ENABLED=0 go build -o /tmp/prometheus_remote_kinesis .

### docker image
FROM alpine:3.7

RUN apk add --no-cache ca-certificates

COPY --from=build-env /tmp/prometheus_remote_kinesis /prometheus_remote_kinesis

ENV AWS_REGION ap-northeast-1
ARG STREAM_NAME

CMD /prometheus_remote_kinesis -stream-name $STREAM_NAME
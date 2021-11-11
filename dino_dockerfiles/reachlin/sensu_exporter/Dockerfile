FROM golang:alpine AS builder
RUN apk add --no-cache git gcc libc-dev
WORKDIR /go/src/github.com/reachlin/sensu_exporter
ENV GO111MODULE=on
COPY go.mod .
COPY go.sum .
RUN go mod download

COPY sensu_exporter.go .
RUN go install .

FROM  golang:alpine
LABEL maintainer="reachlin@gmail.com"

COPY --from=builder /go/bin/sensu_exporter /bin/sensu_exporter

EXPOSE      9104
ENTRYPOINT  [ "/bin/sensu_exporter" ]

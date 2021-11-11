FROM golang:latest as builder

RUN go get -d -v github.com/PierreZ/goStatic
WORKDIR /go/src/github.com/PierreZ/goStatic
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o goStatic .

WORKDIR /tmp/
ARG CONFD_VERSION=0.15.0
ADD https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 /confd
COPY docker/confd /etc/confd
RUN chmod 755 /confd && \
    chmod 755 /etc/confd/confd-wrapper.sh && \
    chmod 755 /go/src/github.com/PierreZ/goStatic/goStatic

FROM alpine:latest
RUN apk --no-cache add ca-certificates bash && mkdir -p /srv/http/.well-known
COPY --from=builder /go/src/github.com/PierreZ/goStatic/goStatic /confd /
COPY --from=builder /etc/confd /etc/confd

CMD ["/etc/confd/confd-wrapper.sh"]

FROM quay.io/giantswarm/golang:1.16.2-alpine3.13 AS builder

COPY . /opt/project

WORKDIR /opt/project

RUN go build .

FROM quay.io/giantswarm/alpine:3.13.5

WORKDIR /opt/slackreader

COPY --from=builder /opt/project/giant-chatops-slack-reader /opt/slackreader/

ENTRYPOINT ["/opt/slackreader/giant-chatops-slack-reader"]

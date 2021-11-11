FROM alpine:3.13.1

RUN apk add --no-cache ca-certificates

ADD ./flannel-operator /flannel-operator

ENTRYPOINT ["/flannel-operator"]

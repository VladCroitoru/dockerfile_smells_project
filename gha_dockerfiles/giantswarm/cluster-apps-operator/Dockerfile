FROM alpine:3.14.2

RUN apk add --no-cache ca-certificates

ADD ./cluster-apps-operator /cluster-apps-operator

ENTRYPOINT ["/cluster-apps-operator"]

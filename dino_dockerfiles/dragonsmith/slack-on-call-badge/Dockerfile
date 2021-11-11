FROM golang:1.10.3-alpine3.8 as builder
WORKDIR /go/src/github.com/dragonsmith/slack-on-call-badge
COPY ./ /go/src/github.com/dragonsmith/slack-on-call-badge/
ENV CGO_ENABLED=0
RUN go build -v -o slack-on-call-badge

FROM  busybox:1.29.1
LABEL Author="Kirill Kuznetsov <agon.smith@gmail.com>"
LABEL version="0.0.3"
COPY --from=builder /go/src/github.com/dragonsmith/slack-on-call-badge/slack-on-call-badge /slack-on-call-badge
ENTRYPOINT ["/slack-on-call-badge"]

# stage 1
FROM golang:1.9.4

COPY Makefile /go/src/github.com/hdpe/mailsling/
COPY cmd/ /go/src/github.com/hdpe/mailsling/cmd/
COPY internal/ /go/src/github.com/hdpe/mailsling/internal/

WORKDIR /go/src/github.com/hdpe/mailsling/
RUN CGO_ENABLED=0 GOOS=linux make

# stage 2
FROM alpine:latest
RUN apk --no-cache add ca-certificates

WORKDIR /root/
COPY --from=0 /go/bin/mailsling .

RUN echo '* * * * * /root/mailsling' >> /var/spool/cron/crontabs/root

CMD ["crond", "-f"]

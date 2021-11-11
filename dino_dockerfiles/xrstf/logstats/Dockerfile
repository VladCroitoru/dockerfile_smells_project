FROM golang:1.10-alpine as builder

RUN apk add --update make git pcre-dev build-base
WORKDIR /go/src/github.com/xrstf/logstats/
COPY . .
RUN make deps static

FROM alpine:3.7

WORKDIR /app
COPY --from=builder /go/src/github.com/xrstf/logstats/cmd/logstats/logstats .
ENTRYPOINT ["./logstats"]

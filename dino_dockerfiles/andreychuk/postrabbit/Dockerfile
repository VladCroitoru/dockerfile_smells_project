FROM golang:1.9.2-alpine3.6
WORKDIR /go/src/postrabbit
COPY . .
RUN apk add --no-cache openssl git && \
    wget -O /usr/bin/dep https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-amd64 && \
    chmod +x /usr/bin/dep /usr/bin/dep && \
    dep ensure -vendor-only && go build

FROM alpine:3.6
MAINTAINER Vanya Andreychuk <vanya@tep.io>
WORKDIR /root/
COPY --from=0 /go/src/postrabbit .
ENV POSTGRES_URL="postgres://user:pass@postgresql:5432/test?sslmode=disable" \
    RABBITMQ_URL="amqp://admin:pass@rabbitmq:5672" \
    CHANNEL_LIST="test,test1,test2"
RUN apk --no-cache add ca-certificates
CMD [ "./postrabbit" ]

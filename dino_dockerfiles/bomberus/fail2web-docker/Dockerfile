FROM golang:alpine

WORKDIR /go/src/app
RUN apk add --no-cache git build-base && \
    go get -v github.com/Sean-Der/fail2rest && \
    go install -v github.com/Sean-Der/fail2rest && \
    echo "{ \"Addr\": \"0.0.0.0:5000\", \"Fail2banSocket\": \"/var/run/fail2ban/fail2ban.sock\" }" >> /etc/config.json
CMD fail2rest --config /etc/config.json

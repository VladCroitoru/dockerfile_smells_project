FROM golang

ADD main.go /tmp/main/
RUN go build -o /usr/bin/gorerun /tmp/main/main.go; rm -rf /tmp/main

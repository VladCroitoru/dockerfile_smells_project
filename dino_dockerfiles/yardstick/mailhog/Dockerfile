FROM golang:1.9
MAINTAINER Daniel Huckstep <danielh@getyardstick.com>

RUN go get github.com/mailhog/MailHog

EXPOSE 80 25

CMD /go/bin/MailHog -api-bind-addr 0.0.0.0:80 -ui-bind-addr 0.0.0.0:80 -smtp-bind-addr 0.0.0.0:25

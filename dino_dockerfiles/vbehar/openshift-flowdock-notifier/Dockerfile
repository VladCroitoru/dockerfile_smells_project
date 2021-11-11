FROM golang:1.6

MAINTAINER https://github.com/vbehar/openshift-flowdock-notifier

ENV GOPATH=/go/src/github.com/vbehar/openshift-flowdock-notifier/Godeps/_workspace:/go

COPY . /go/src/github.com/vbehar/openshift-flowdock-notifier/

RUN go install github.com/vbehar/openshift-flowdock-notifier

RUN mv /go/bin/openshift-flowdock-notifier /openshift-flowdock-notifier

WORKDIR "/"

CMD [ "/openshift-flowdock-notifier" ]

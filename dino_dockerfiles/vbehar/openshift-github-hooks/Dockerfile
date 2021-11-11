FROM golang:1.6

MAINTAINER https://github.com/vbehar/openshift-github-hooks

ENV GOPATH=/go/src/github.com/vbehar/openshift-github-hooks/Godeps/_workspace:/go \
    PATH=/go/bin:$PATH

COPY . /go/src/github.com/vbehar/openshift-github-hooks/

RUN go install github.com/vbehar/openshift-github-hooks

WORKDIR "/"

CMD [ "openshift-github-hooks" ]

FROM golang:1.8

ADD . /go/src/github.com/Fahrradflucht/last-supper
WORKDIR /go/src/github.com/Fahrradflucht/last-supper
RUN go get && go install

ENTRYPOINT /go/bin/last-supper -port 80

EXPOSE 80

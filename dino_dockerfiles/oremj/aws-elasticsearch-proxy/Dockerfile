FROM golang:1.7

ENV PROJECT=github.com/oremj/aws-elasticsearch-proxy

COPY . /go/src/$PROJECT

EXPOSE 8000

RUN go install $PROJECT

ENTRYPOINT ["aws-elasticsearch-proxy"]

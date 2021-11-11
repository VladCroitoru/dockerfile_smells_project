FROM golang:alpine

EXPOSE 80

RUN apk --no-cache add ca-certificates && update-ca-certificates

RUN mkdir -p /go/src/github.com/fardog/reverseoperator
COPY . /go/src/github.com/fardog/reverseoperator

WORKDIR /go/src/github.com/fardog/reverseoperator/cmd/reverse-operator
RUN go install -v

CMD reverse-operator --listen 0.0.0.0:80

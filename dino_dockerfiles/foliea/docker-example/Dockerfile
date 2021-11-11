FROM golang:1.4

ENV APP $GOPATH/src/foliea/docker-example

COPY . $APP

WORKDIR $APP

CMD ["go", "run", "main.go"]

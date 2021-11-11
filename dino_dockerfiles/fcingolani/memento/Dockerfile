FROM golang:1.8-alpine

EXPOSE 3000

WORKDIR /go/src/github.com/fcingolani/memento
COPY . /go/src/github.com/fcingolani/memento

RUN apk update \
    && apk --update --no-cache add git gcc musl-dev \
    && go-wrapper download \
    && go-wrapper install \
    && apk del git gcc musl-dev

CMD ["go-wrapper", "run"]
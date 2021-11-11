FROM golang:alpine

RUN apk add --no-cache git

RUN mkdir -p /go/src/app
WORKDIR /go/src/app

COPY . /go/src/app
RUN go-wrapper download
RUN go-wrapper install

# this will ideally be built by the ONBUILD below ;)
CMD ["go-wrapper", "run"]

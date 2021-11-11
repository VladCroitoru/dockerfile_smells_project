FROM golang:1.8-alpine

RUN mkdir -p /go/src/app
WORKDIR /go/src/app

COPY . /go/src/app
RUN go-wrapper download
RUN go-wrapper install

EXPOSE 8000
CMD ["go-wrapper", "run"]

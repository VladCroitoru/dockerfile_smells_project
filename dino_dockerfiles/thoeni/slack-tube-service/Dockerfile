FROM golang

RUN mkdir -p /go/src/app
WORKDIR /go/src/app

ADD . /go/src/app
RUN go-wrapper download
RUN go-wrapper install

CMD ["go-wrapper", "run"]

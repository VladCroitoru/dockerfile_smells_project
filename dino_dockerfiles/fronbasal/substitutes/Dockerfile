FROM golang:latest

RUN mkdir /go/src/substitutes
WORKDIR /go/src/substitutes
ADD . /go/src/substitutes

RUN go get -v -d .
RUN go install -v .

CMD ["substitutes"]

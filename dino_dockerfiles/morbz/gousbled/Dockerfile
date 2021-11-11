FROM golang:1

WORKDIR /go/src/app
COPY . .

RUN go get
RUN go install

CMD ["app"]

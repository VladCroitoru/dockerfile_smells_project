FROM golang:1.8
MAINTAINER Abdulkadir Yaman <abdulkadiryaman@gmail.com>

WORKDIR /go/src/app
COPY . .

RUN go-wrapper download
RUN go-wrapper install

CMD ["go-wrapper", "run"]

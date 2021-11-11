FROM golang:1.5

RUN mkdir -p /go/src/monitor
COPY . /go/src/monitor
WORKDIR /go/src/monitor

RUN go-wrapper download
RUN go-wrapper install

ENTRYPOINT ["go-wrapper", "run"]

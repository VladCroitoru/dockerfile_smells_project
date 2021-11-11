FROM golang:1.4

RUN mkdir -p /go/src/github.com/mfellner/comodoro
WORKDIR /go/src/github.com/mfellner/comodoro

COPY . /go/src/github.com/mfellner/comodoro
RUN go-wrapper download
RUN go-wrapper install

ENV APP_PORT 3030
ENV APP_LOGLEVEL info
ENV APP_FLEETENDPOINT unix:///var/run/fleet.sock

CMD ["go-wrapper", "run"]

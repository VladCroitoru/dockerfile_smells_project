FROM golang

LABEL MAINTAINER "Fernando Ike <fike@midstorm.org>"

COPY helloapp.go .

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o helloapp .

FROM alpine:latest

COPY --from=0 $HOME/go/helloapp /usr/bin/

ENTRYPOINT  /usr/bin/helloapp

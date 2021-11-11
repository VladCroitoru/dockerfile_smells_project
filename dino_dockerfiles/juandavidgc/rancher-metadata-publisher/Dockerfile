FROM golang:1.5

ADD ./scripts/bootstrap /scripts/bootstrap
RUN chmod +x -R /scripts/
RUN /scripts/bootstrap

RUN mkdir -p /go/src/proxy
ADD main.go /go/src/proxy/main.go
RUN go install proxy
WORKDIR /go/src/proxy/
CMD ["go", "run", "main.go"]

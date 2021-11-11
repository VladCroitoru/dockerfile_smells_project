FROM golang:1.16-stretch

WORKDIR /go/src/github.com/rebelo0512/clinic-project

ENV PATH="/go/bin:${PATH}"

ENV CGO_ENABLE=0

RUN go mod init

CMD ["tail", "-f", "/dev/null"]
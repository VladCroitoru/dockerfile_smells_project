FROM golang:1.7

RUN mkdir /code/
WORKDIR /code/

ADD whatsmyip.go .
RUN go build whatsmyip.go

EXPOSE "80"

ENTRYPOINT ["/code/whatsmyip"]

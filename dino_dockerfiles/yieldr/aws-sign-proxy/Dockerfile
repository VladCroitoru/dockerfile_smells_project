FROM golang:1.8

WORKDIR /go/src/app
COPY . /go/src/app

RUN make deps && make
RUN cp /go/src/app/bin/aws-sign-proxy /usr/bin

CMD ["aws-sign-proxy"]

FROM golang:1.8.3-alpine

ADD . /go/src/github.com/anarcher/mockingjay

RUN cd /go/src/github.com/anarcher/mockingjay/cmd/mj && go install
RUN cd /go/src/github.com/anarcher/mockingjay/examples/aws-cloudwatch/mock && go install

WORKDIR /go/bin

CMD mj

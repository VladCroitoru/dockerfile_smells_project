FROM golang

ADD  . /go/src/calpi
RUN go get -u github.com/aws/aws-sdk-go
RUN cd /go/src/calpi &&\
    go build &&\
    go install
CMD calpi

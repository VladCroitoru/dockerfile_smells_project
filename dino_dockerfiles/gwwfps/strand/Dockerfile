FROM golang
ADD . /go/src/github.com/gwwfps/strand
RUN go get github.com/kelseyhightower/envconfig
RUN go install github.com/gwwfps/strand
ENTRYPOINT /go/bin/strand

EXPOSE 8080

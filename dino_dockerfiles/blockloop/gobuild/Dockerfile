FROM golang:1

ADD https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-amd64 /usr/local/bin/dep
RUN chmod +x /usr/local/bin/dep
RUN go get -u gopkg.in/alecthomas/gometalinter.v1
RUN mv /go/bin/gometalinter.v1 /go/bin/gometalinter
RUN gometalinter -i

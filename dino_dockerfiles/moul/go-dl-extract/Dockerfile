FROM golang:1.4-cross

ENV CGO_ENABLED 0

# Recompile the standard library without CGO
RUN go install -a std

# Declare the maintainer
MAINTAINER Manfred Touron @moul

# For convenience, set an env variable with the path of the code
ENV APP_DIR /go/src/github.com/moul/go-dl-extract
WORKDIR $APP_DIR
ADD . /go/src/github.com/moul/go-dl-extract

# Compile the binary and statically link
RUN GOOS=darwin GOARCH=amd64          go build -a -v -ldflags '-w -s' -o /go/bin/go-dl-extract-Darwin-x86_64
RUN GOOS=linux  GOARCH=amd64          go build -a -v -ldflags '-w -s' -o /go/bin/go-dl-extract-Linux-x86_64
RUN GOOS=linux  GOARCH=386            go build -a -v -ldflags '-w -s' -o /go/bin/go-dl-extract-Linux-i386
RUN GOOS=linux  GOARCH=arm   GOARM=5  go build -a -v -ldflags '-w -s' -o /go/bin/go-dl-extract-Linux-armv5
RUN GOOS=linux  GOARCH=arm   GOARM=6  go build -a -v -ldflags '-w -s' -o /go/bin/go-dl-extract-Linux-armv6
RUN GOOS=linux  GOARCH=arm   GOARM=7  go build -a -v -ldflags '-w -s' -o /go/bin/go-dl-extract-Linux-armv7

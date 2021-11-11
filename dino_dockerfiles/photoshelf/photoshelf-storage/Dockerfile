FROM golang:alpine
MAINTAINER shunsuke maeda <duck8823@gmail.com>

RUN apk --update add --no-cache git

WORKDIR /go/src/github.com/photoshelf/photoshelf-storage

ADD . .

RUN go get -u github.com/golang/dep/cmd/dep && \
    dep ensure

RUN go build

RUN mkdir -p /photoshelf/photos
VOLUME /photoshelf/photos

EXPOSE 1323

CMD ["./photoshelf-storage", "-s", "/photoshelf/photos/db"]

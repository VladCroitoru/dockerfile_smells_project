FROM golang:1.17
LABEL maintainer="Jason Ross <algorythm@gmail.com>"

ARG GOOS
ARG GOARCH

ENV GOOS=$GOOS
ENV GOARCH=$GOARCH

WORKDIR /go/src/app

COPY src ./

RUN go mod init
RUN go get -d -v ./...
RUN go install -v ./...

CMD ["app"]

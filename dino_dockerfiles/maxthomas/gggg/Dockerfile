FROM golang:latest

RUN apt-get update -qq -y && apt-get install curl -y
RUN curl https://glide.sh/get | sh
RUN go get github.com/mitchellh/gox
RUN go get github.com/tcnksm/ghr



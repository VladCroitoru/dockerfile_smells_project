FROM golang:1.7-alpine
MAINTAINER mdouchement

ENV ECHO_ENV production
ENV LSS_WORKSPACE /data/workspace

RUN mkdir -p $LSS_WORKSPACE

RUN apk upgrade
RUN apk add --update --no-cache git
RUN go get github.com/Masterminds/glide

WORKDIR /go/src/github.com/mdouchement/lss

COPY . /go/src/github.com/mdouchement/lss
RUN glide install
RUN go install github.com/mdouchement/lss

EXPOSE 8080
CMD ["lss", "server", "-p", "8080"]

FROM golang:1.9.2-alpine3.6
RUN apk update && apk upgrade && \
    apk add --no-cache git
RUN go get -u github.com/golang/dep/cmd/dep
ENTRYPOINT ["dep"]

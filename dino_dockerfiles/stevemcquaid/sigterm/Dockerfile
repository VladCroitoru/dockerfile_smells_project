FROM golang:1.8.5-alpine3.6

MAINTAINER Steve McQuaid <steve@stevemcquaid.com>

RUN apk update && apk upgrade && \
    apk add --no-cache bash git

WORKDIR /go/src/sigterm

COPY src/* .

RUN go-wrapper download   # "go get -d -v ./..."
RUN go-wrapper install    # "go install -v ./..."

CMD ["go-wrapper", "run"] # ["app"]
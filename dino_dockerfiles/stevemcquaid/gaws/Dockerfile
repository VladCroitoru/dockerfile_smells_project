FROM golang:1.8.5-alpine3.6

MAINTAINER Steve McQuaid <steve@stevemcquaid.com>

ENV VERSION=1.0.0

RUN apk update && apk upgrade && \
    apk add --no-cache bash git

WORKDIR /go/src/gaws

# Caching large packages to speed up build
RUN go-wrapper download -u golang.org/x/crypto/ssh/terminal 
RUN go-wrapper download -u github.com/golang/glog
RUN go-wrapper download -u github.com/aws/aws-sdk-go
RUN go-wrapper download -u k8s.io/kops/upup/pkg/fi

COPY src/ .

RUN go-wrapper download   # "go get -d -v ./..."
RUN go-wrapper install    # "go install -v ./..."

CMD ["go-wrapper", "run"] # ["app"]

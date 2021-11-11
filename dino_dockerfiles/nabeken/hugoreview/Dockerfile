FROM golang:1.3
MAINTAINER TANABE Ken-ichi <nabeken@tknetworks.org>

# Cache heavy git repository such as docker repository
RUN go-wrapper download \
  github.com/docker/docker \
  github.com/fsouza/go-dockerclient \
  github.com/Sirupsen/logrus \
  github.com/garyburd/redigo || :

RUN mkdir -p /go/src/app
WORKDIR /go/src/app

COPY . /go/src/app
RUN go-wrapper download -t ./...
RUN go install ./...

ENTRYPOINT ["hugoreview"]

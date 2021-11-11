FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y wget
RUN wget -O- http://neuro.debian.net/lists/trusty.de-md.full | tee /etc/apt/sources.list.d/neurodebian.sources.list
RUN apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9
RUN apt-get update
RUN apt-get install -y \
    git \
    git-annex-standalone\
    golang

RUN mkdir /go
ENV GOPATH /go
RUN go get gopkg.in/yaml.v2
RUN go get github.com/Sirupsen/logrus
RUN go get github.com/docopt/docopt-go
RUN go get github.com/G-Node/gin-core/gin
RUN go get golang.org/x/crypto/ssh
RUN go get github.com/gogits/go-gogs-client

ADD . /gin-doi
RUN mkdir -p /go/src/github.com/G-Node
RUN ln -s  /gin-doi /go/src/github.com/G-Node/gin-doi
RUN cd gin-doi
WORKDIR /gin-doi
RUN go build

VOLUME ["/doidata"]
VOLUME ["/repos"]

ENTRYPOINT ./gin-doi --debug --target /doidata --gitsource=/repos
EXPOSE 8083
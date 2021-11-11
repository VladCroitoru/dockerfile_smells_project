FROM ubuntu:trusty
MAINTAINER tubesandlube <tubes@tubesandlube.com>

RUN apt-get install -y wget

RUN wget 'http://go.googlecode.com/files/go1.2.1.linux-amd64.tar.gz'
RUN tar -C / -xzf go1.2.1.linux-amd64.tar.gz

ENV GOROOT /go
ENV GOPATH /usr/local/go
ENV PATH $PATH:$GOPATH/bin:$GOROOT/bin

ADD . /usr/local/go/src/dockerlint
RUN go install dockerlint

ENTRYPOINT ["/usr/local/go/bin/dockerlint"]
CMD ["/usr/local/go/src/dockerlint/Dockerfile"]

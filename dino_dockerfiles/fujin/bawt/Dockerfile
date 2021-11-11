FROM ubuntu
MAINTAINER AJ Christensen <aj@junglist.io>

# Setup Go 1.3
ADD http://golang.org/dl/go1.3.linux-amd64.tar.gz /tmp/go.tgz
RUN tar -C /usr/local -xzf /tmp/go.tgz

ADD . /bawt/src/github.com/fujin/bawt
WORKDIR /bawt/src/github.com/fujin/bawt

ENV GOROOT /usr/local/go
ENV GOPATH /bawt
ENV PATH /usr/local/go/bin:$PATH

RUN apt-get update -qq
RUN apt-get install git bzr mercurial -yqq

RUN GOPATH=/bawt go get -v
RUN chmod +x bawt.sh
ENTRYPOINT ["/bawt/src/github.com/fujin/bawt/bawt.sh"]

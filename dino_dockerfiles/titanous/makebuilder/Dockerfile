FROM stackbrew/ubuntu:13.10
MAINTAINER Jeff Lindsay <progrium@gmail.com>

RUN apt-get update; apt-get install -y build-essential curl wget git mercurial bzr
RUN cd /usr/bin && curl -sL j.mp/godeb | tar -xzC . && ./godeb install 1.2
RUN mkdir /tmp/go && \
    GOPATH=/tmp/go go get github.com/kr/godep && \
    mv /tmp/go/bin/godep /usr/bin && \
    rm -rf /tmp/go
ADD ./makebuild /usr/bin/makebuild

CMD makebuild

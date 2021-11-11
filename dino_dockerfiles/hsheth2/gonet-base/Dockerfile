FROM golang:1.6
# named hsheth2/gonet-base

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils sudo net-tools iptables && rm -rf /var/lib/apt/lists/*
RUN go get golang.org/x/tools/cmd/...

#RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
#USER docker

# VOLUME ["/go/src/github.com/hsheth2/gonet"]
# ADD . /go/src/github.com/hsheth2/gonet

CMD /bin/bash


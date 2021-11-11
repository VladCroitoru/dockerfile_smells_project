FROM golang:1.4

RUN useradd pipe && \
  go get github.com/tools/godep && \
  chown -R pipe:pipe /go

#USER pipe

ADD ./Godeps /go/src/github.com/rackerlabs/cloudpipe-rackspace-auth-store/Godeps
WORKDIR /go/src/github.com/rackerlabs/cloudpipe-rackspace-auth-store/
RUN godep restore

ADD . /go/src/github.com/rackerlabs/cloudpipe-rackspace-auth-store/
RUN go install github.com/rackerlabs/cloudpipe-rackspace-auth-store/

CMD ["/go/bin/cloudpipe-rackspace-auth-store"]

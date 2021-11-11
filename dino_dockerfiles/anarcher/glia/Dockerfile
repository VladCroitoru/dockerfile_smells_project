FROM golang:1.6.2

WORKDIR /go/src/github.com/anarcher/glia
ADD . /go/src/github.com/anarcher/glia
RUN ./.build_version
RUN go install -ldflags="-X main.Version=`cat ./VERSION` -X main.GitCommit=`git rev-parse --short HEAD`" -v 

ENTRYPOINT ["glia"]

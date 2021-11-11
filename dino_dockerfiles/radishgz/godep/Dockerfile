FROM golang
RUN go get github.com/tools/godep
RUN go get github.com/gregjones/httpcache
RUN go get github.com/davecgh/go-spew/spew
RUN go get github.com/ghodss/yaml
RUN go get github.com/gogo/protobuf/proto
RUN go get github.com/golang/protobuf/proto
RUN go get github.com/google/btree
RUN go get github.com/googleapis/gnostic/OpenAPIv2
RUN go get github.com/gregjones/httpcache
RUN go get github.com/peterbourgon/diskv
RUN go get github.com/hashicorp/golang-lru
RUN go get github.com/json-iterator/go
RUN go get github.com/juju/ratelimit
RUN go get github.com/spf13/pflag
RUN go get golang.org/x/net/context
RUN  mkdir -p $GOPATH/src/golang.org/x
RUN cd $GOPATH/src/golang.org/x
RUN git clone https://github.com/golang/tools
RUN go get golang.org/x/text/secure/bidirule
#RUN go get golang.org/x/tools
RUN go get go.uber.org/zap
RUN go get gopkg.in/inf.v0
RUN go get gopkg.in/yaml.v2
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh

FROM  golang:1.7.5


RUN go get github.com/progrium/go-shell
RUN go get github.com/prometheus/promu
#RUN go get github.com/golang/protobuf
RUN go get -u github.com/prometheus/common/route

#RUN go get github.com/prometheus/alertmanager/

# cd $GOPATH/src/github.com/prometheus/alertmanager

#RUN mkdir -p $GOPATH/src/github.com/prometheus \
#  && cd $GOPATH/src/github.com/prometheus \
# && git clone https://github.com/prometheus/alertmanager
#ADD ./alertmanager $GOPATH/src/github.com/prometheus/alertmanager
#RUN cd $GOPATH/src/github.com/prometheus/alertmanager \
#&&  make build

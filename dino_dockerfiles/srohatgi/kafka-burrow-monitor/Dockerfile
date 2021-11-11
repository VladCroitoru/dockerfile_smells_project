FROM magnetme/burrow:latest

MAINTAINER sumeet rohatgi

ADD . $GOPATH/src/github.com/srohatgi/kafka-burrow-monitor
RUN cd $GOPATH/src/github.com/srohatgi/kafka-burrow-monitor &&\
  go install &&\
  mv $GOPATH/bin/kafka-burrow-monitor /go/bin/kafka-burrow-monitor

ENV PATH=$PATH:$GOPATH/bin

WORKDIR /var/tmp/burrow

CMD sleep 150 && /go/bin/kafka-burrow-monitor

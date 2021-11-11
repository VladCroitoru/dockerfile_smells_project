FROM mischief/docker-golang
ENV HOME /root

RUN apt-get -q update && apt-get install -y pkg-config libxml2-dev

RUN go get github.com/nutrun/lentil
RUN go get github.com/vierja/logprecios-parsers
RUN mkdir -p $GOPATH/src/github.com/vierja/logprecios-savages
ADD . $GOPATH/src/github.com/vierja/logprecios-savages

WORKDIR /root
RUN go build github.com/vierja/logprecios-savages

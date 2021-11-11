  
FROM golang

WORKDIR /go/src/github.com/san-lab
RUN git clone https://github.com/san-lab/cc2 && git clone https://github.com/san-lab/commongo
RUN cd /go/src/github.com/san-lab/cc2/confisum && rm -f confisum && go build
ENV httpPort "8080"
WORKDIR /go/src/github.com/san-lab/cc2/confisum
CMD ./confisum -httpPort=$httpPort

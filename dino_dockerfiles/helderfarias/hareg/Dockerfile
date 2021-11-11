FROM golang

RUN curl -L https://github.com/Masterminds/glide/releases/download/0.10.2/glide-0.10.2-linux-amd64.tar.gz > glide.tar.gz \
    && tar xvzf glide.tar.gz \
    && cp linux-amd64/glide /usr/bin/glide \
    && rm -rf linux-amd64  
    
RUN mkdir -p cd $GOPATH/src/github.com/helderfarias/hareg
COPY discovery $GOPATH/src/github.com/helderfarias/hareg/discovery
COPY model $GOPATH/src/github.com/helderfarias/hareg/model
COPY register $GOPATH/src/github.com/helderfarias/hareg/register
COPY util $GOPATH/src/github.com/helderfarias/hareg/util
COPY main.go $GOPATH/src/github.com/helderfarias/hareg/
COPY glide.yaml $GOPATH/src/github.com/helderfarias/hareg/glide.yaml

RUN cd src/github.com/helderfarias/hareg \
    && glide install \
    && go build
    
RUN cd src/github.com/helderfarias/hareg \
    && cp hareg /usr/bin/hareg \
    && chmod +x /usr/bin/hareg \
    && rm -rf src/* \
    && /usr/bin/glide

ENTRYPOINT ["/usr/bin/hareg"]

FROM alpine:3.3

ENV GOPATH=/go PATH=/go/bin:$PATH

COPY . $GOPATH/src/github.com/toksaitov/auca-judge-agent
WORKDIR $GOPATH/src/github.com/toksaitov/auca-judge-agent

RUN apk add --no-cache git go && \
    go get -d                 && \
    apk del git               && \
    go install                && \
    apk del go                && \
    rm -rf "$GOPATH/pkg" "$GOPATH/src"

ONBUILD COPY auca-judge-agent-configuration.json /agent/
WORKDIR /agent

CMD ["/go/bin/auca-judge-agent"]

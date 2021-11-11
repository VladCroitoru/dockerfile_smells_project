FROM golang:1.7.1

COPY . /go/src/github.com/botyard/botyard/
WORKDIR /go/src/github.com/botyard/botyard
RUN go install  -ldflags="-X main.version=`git describe --tags` -X main.buildTime=`date -u '+%Y-%m-%d_%I:%M:%S%p'` -X main.gitCommit=`git rev-parse --short HEAD`" -v

ENTRYPOINT ["botyard"]

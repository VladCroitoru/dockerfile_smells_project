# we need this image
FROM golang:1.5.3

RUN apt-get update -qq && \
    apt-get install -y postgresql-client-9.4

RUN go get "github.com/kruszczynski/barkup" \
           "launchpad.net/goamz/s3" \
           "github.com/jasonlvhit/gocron"

ENV APP_HOME=${GOPATH}/src/github.com/lunchiatto/backuper
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME
ADD . $APP_HOME

# Build dependencies and the ws binary
RUN go build
CMD ["./backuper"]

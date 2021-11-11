FROM golang:1.8

RUN mkdir /data
COPY . "$GOPATH/src/github.com/weirdsnap/upgraded-agenda/"
RUN cd "$GOPATH/src/github.com/weirdsnap/upgraded-agenda/service" && go get -v && go install -v
RUN cd "$GOPATH/src/github.com/weirdsnap/upgraded-agenda/cli" && go get -v && go install -v

EXPOSE 8080

VOLUME /data



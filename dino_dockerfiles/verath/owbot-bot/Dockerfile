# Dockerfile for owbot-bot
#
# docker build . -t vearth/owbot-bot

FROM golang:1.10-alpine

COPY . /go/src/github.com/verath/owbot-bot

ARG GIT_REVISION="master"

RUN go install -ldflags "-X github.com/verath/owbot-bot/owbot.gitRevision=${GIT_REVISION}" github.com/verath/owbot-bot

RUN rm -rf /go/src

VOLUME /db

STOPSIGNAL SIGINT

ENTRYPOINT ["owbot-bot", "-dbfile", "/db/owbot.boltdb"]

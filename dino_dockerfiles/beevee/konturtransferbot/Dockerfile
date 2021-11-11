FROM golang:1.15-alpine as golang
WORKDIR /go/src/github.com/beevee/konturtransferbot
COPY . .
RUN apk add --no-cache git mercurial \
    && go get github.com/kardianos/govendor \
    && govendor sync \
    && apk del git mercurial
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /go/bin/konturtransferbot github.com/beevee/konturtransferbot/cmd/konturtransferbot

FROM alpine
RUN apk add --no-cache tzdata ca-certificates && update-ca-certificates
COPY cmd/konturtransferbot/schedule.yml /schedule.yml
COPY --from=golang /go/bin/konturtransferbot /konturtransferbot
ENTRYPOINT ["/konturtransferbot"]

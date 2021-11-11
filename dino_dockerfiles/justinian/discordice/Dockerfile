FROM golang:1.9.2

RUN go get github.com/golang/dep/... && go install github.com/golang/dep/...

ADD . /go/src/github.com/justinian/discordice
WORKDIR /go/src/github.com/justinian/discordice
RUN dep ensure
RUN CGO_ENABLED=0 go build -a -o discordice .


FROM alpine:latest
MAINTAINER Justin C. Miller <justin@devjustinian.com>

RUN apk --no-cache add ca-certificates
COPY --from=0 /go/src/github.com/justinian/discordice/discordice /
ENTRYPOINT ["/discordice"]

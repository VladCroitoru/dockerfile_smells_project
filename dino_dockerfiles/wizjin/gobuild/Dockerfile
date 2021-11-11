FROM golang:alpine
MAINTAINER WizJin <wizjin@users.noreply.github.com>
RUN apk add --update --no-cache git make findutils gcc musl-dev \
  && go get github.com/wadey/gocovmerge \
  && go get github.com/streadway/amqp \
  && go get github.com/globalsign/mgo \
  && go get github.com/spf13/cobra \
  && go get github.com/spf13/viper \
  && go get github.com/mitchellh/go-homedir \
  && go get github.com/gorilla/mux \
  && go get github.com/julienschmidt/httprouter \
  && go get golang.org/x/sys/unix \
  && go get golang.org/x/text/transform \
  && go get golang.org/x/text/unicode \
  && go get golang.org/x/crypto/...

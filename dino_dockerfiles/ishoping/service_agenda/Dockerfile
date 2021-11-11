FROM golang:1.8

RUN mkdir -p /go/src/service_agenda
RUN mkdir -p /go/bin
Run mkdir -p /go/pkg
RUN apt-get update && apt-get install -y --no-install-recommends \
		apt-utils \
		sqlite3

RUN go get -d -v \
	github.com/codegangsta/negroni \
	github.com/go-xorm/xorm \
	github.com/gorilla/mux \
	github.com/mattn/go-sqlite3 \
	github.com/spf13/pflag \
	github.com/unrolled/render \
	github.com/mitchellh/go-homedir \
	github.com/spf13/viper

RUN go get -v \
	github.com/spf13/cobra

VOLUME ["/go/src/service_agenda/data"]
ADD . /go/src/service_agenda

WORKDIR /go/src/service_agenda

RUN go build -o server .

WORKDIR cli
RUN go build -o cli .

WORKDIR /go/src/service_agenda/cli

EXPOSE 8080

CMD ["/go/src/service_agenda/server"]
FROM golang:latest

RUN apt-get update && \
    apt-get install -y sqlite3 libsqlite3-dev

RUN mkdir /go/src/AgendaService

VOLUME "/go/db/"

COPY . /go/src/AgendaService

# use only on local test
# ENV http_proxy="socks5://192.168.199.116:4321" \
#   https_proxy="socks5://192.168.199.116:4321"

RUN go get -v AgendaService/service AgendaService/cli && \
    go install AgendaService/service && go install AgendaService/cli

VOLUME [ "/go" ]

EXPOSE 8080

ENTRYPOINT [ "/bin/sh", "/go/src/AgendaService/docker-entry.sh" ]

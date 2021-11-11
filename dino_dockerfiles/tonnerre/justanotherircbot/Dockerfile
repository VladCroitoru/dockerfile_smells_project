FROM debian:stretch
MAINTAINER Juliane Clausen <github@juliane-clausen.de>

ENV GOPATH /usr/share/gocode:/usr/local
VOLUME ["/etc/justanotherircbot"]

# Apply changes so we can install golang.
RUN apt-get -q -y update
RUN apt-get -q -y -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold --purge install golang-go golang-golang-x-net-dev golang-golang-x-tools golang-golang-x-tools-dev golang-goprotobuf-dev golang-x-text-dev git-core mercurial protobuf-compiler

# Install the missing IRC bot dependencies.
RUN go get github.com/thoj/go-ircevent
RUN mkdir -p /usr/local/src/github.com/julianec
RUN cd /usr/local/src/github.com/julianec && git clone https://github.com/julianec/justanotherircbot.git
RUN cd /usr/local/src/github.com/julianec/justanotherircbot && protoc --go_out=. config.proto
RUN cd /usr/local/src/github.com/julianec/justanotherircbot && go build
RUN cd /usr/local/src/github.com/julianec/justanotherircbot && go install

RUN addgroup --quiet --system --force-badname _ircbot
RUN adduser --quiet --system --ingroup _ircbot --disabled-login --disabled-password --home /nonexistent --no-create-home --force-badname --gecos "Just another IRC bot" _ircbot

# Default is to run justanotherircbot.
USER _ircbot
ENTRYPOINT ["/usr/local/bin/justanotherircbot"]
CMD ["--config=/etc/justanotherircbot/justanotherircbot.conf"]

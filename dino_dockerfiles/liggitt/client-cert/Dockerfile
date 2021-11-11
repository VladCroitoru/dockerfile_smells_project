# Clone from the Fedora 22 image
FROM golang:latest

MAINTAINER Jordan Liggitt <jliggitt@redhat.com>

EXPOSE 9443

CMD    ["go","run","server.go"]

ADD localhost.crt localhost.crt
ADD localhost.key localhost.key
ADD server.go server.go

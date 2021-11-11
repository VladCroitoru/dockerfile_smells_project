# Docker container containing toml2json

FROM golang:1.8 as build-toml2json
RUN go get github.com/creack/toml2json

FROM alpine:3.6
MAINTAINER Jason Crowe <jcrowe@mozilla.com>
COPY --from=build-toml2json /go/bin/toml2json /usr/local/bin/

CMD [ "toml2json" ]

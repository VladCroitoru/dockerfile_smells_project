# Docker go-configurator
# Wills Ward
# 03/31/16

FROM golang:1.13

MAINTAINER William Ward <wills.e.ward@tcu.edu>

ONBUILD ADD ./templates /var/go-configurator/templates
ONBUILD ADD ./config.yml /var/go-configurator/config.yml
ONBUILD ADD ./before.sh /var/go-configurator/before.sh
ONBUILD ADD ./after.sh /var/go-configurator/after.sh

# Build binary
RUN go get github.com/willseward/go-configurator
RUN go get -v ./...
RUN go install -v github.com/willseward/go-configurator

ENTRYPOINT ["/go/bin/go-configurator"]

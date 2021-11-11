FROM golang:latest
EXPOSE 9000

LABEL maintainer="kterada.0509sg@gmail.com"

RUN set -x \
    # go get revel
    && go get -v github.com/revel/revel \
    && go get -v github.com/revel/cmd/revel

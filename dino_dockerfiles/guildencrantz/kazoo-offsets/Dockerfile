FROM golang:1.5.3-onbuild

ENTRYPOINT [ "/kazoo-offsets/kazoo-offsets" ]
WORKDIR /kazoo-offsets

ADD . /kazoo-offsets
RUN go build

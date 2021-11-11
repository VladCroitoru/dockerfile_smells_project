FROM golang:alpine
MAINTAINER "aerth <aerth@riseup.net>

RUN apk add --update --no-cache git bash vim htop tmux curl musl-dev

ENV PATH="/root/go/bin:/root/bin:${PATH}"
ENV GOBIN="/root/go/bin"
ENV CGO_ENABLED=0
ADD bashrc /root/.bashrc

RUN curl https://gitlab.com/aerth/dot/-/raw/master/auto_install | bash
RUN vim -c ":GoInstallBinaries" -c q\! main.go

RUN apk add --update --no-cache gcc file tree valgrind gdb make

ENV CGO_ENABLED=
RUN rm -rf /go/pkg /root/.cache

WORKDIR /src
ENTRYPOINT bash

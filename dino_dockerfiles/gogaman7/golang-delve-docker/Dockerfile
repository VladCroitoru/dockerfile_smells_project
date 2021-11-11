FROM golang

RUN chsh -s /bin/bash
RUN mkdir /app
RUN go get github.com/derekparker/delve/cmd/dlv
ENV GOPATH=/go:/app
ENV PATH=$PATH:/app

VOLUME /app
WORKDIR /app

FROM alpine:latest

LABEL maintainer "klazutin@gmail.com"
ARG LEANOTE_VER=2.4

RUN apk --update add curl
RUN curl -L http://sourceforge.net/projects/leanote-bin/files/$LEANOTE_VER/leanote-linux-amd64-v$LEANOTE_VER.bin.tar.gz/download > leanote.tar.gz
RUN gunzip leanote.tar.gz
RUN tar xvf leanote.tar

ENV GOPATH /leanote
RUN mkdir -p /leanote/src/github.com/leanote
RUN ln -s /leanote /leanote/src/github.com/leanote/
RUN ln -s /leanote/bin/src/github.com/revel/ /leanote/src/github.com/revel

RUN rm /leanote/conf/app.conf
COPY ./app.conf /leanote/conf/

EXPOSE 9000

CMD ["/leanote/bin/leanote-linux-amd64", "-importPath", "github.com/leanote/leanote"]
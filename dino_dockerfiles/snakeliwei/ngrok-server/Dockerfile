FROM golang:1.7
MAINTAINER lyndon <snakeliwei@gmail.com>

RUN apt-get update && \
    apt-get install -y build-essential git mercurial && \
    mkdir -p /release

RUN git clone https://github.com/inconshreveable/ngrok.git /ngrok

COPY . /

ENV GOOS ""
ENV GOARCH "" 
ENV DOMAIN **None**

VOLUME ["/ngrok/bin"]
CMD ["/build.sh"]

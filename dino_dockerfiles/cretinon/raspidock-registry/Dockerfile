FROM resin/raspberrypi3-golang

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install curl git mercurial make  binutils bison gcc build-essential
RUN cd /go/src ; git clone https://github.com/docker/distribution.git
RUN cd /go/src/distribution ; go get -d ./...
RUN cd /go/src/distribution ; GOOS=linux GOARCH=arm make binaries
RUN mkdir -p /var/lib/registry

EXPOSE 5000/tcp

CMD ["/go/src/distribution/bin/registry", "serve", "/tmp/registry-config.yml"]

RUN [ "cross-build-end" ]  

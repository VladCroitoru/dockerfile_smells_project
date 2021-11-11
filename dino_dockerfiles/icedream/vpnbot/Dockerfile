FROM golang:1.5.3-alpine
MAINTAINER Carl Kittelberger <icedream@icedream.pw>

WORKDIR /go/src/github.com/icedream/vpnbot
COPY . /go/src/github.com/icedream/vpnbot
RUN \
	apk update &&\
	apk add git &&\
	export GOPATH="/go" &&\
	export GOBIN="/usr/local/bin" &&\
	go get -v -ldflags "-X main.version=$(git describe --tags --always --long) -s -extldflags -static" &&\
	apk del git &&\
	cd / &&\
	rm -rf /tmp/* /var/tmp/* /var/cache/apk /etc/apk/cache /go
WORKDIR /data

# dumb-init
ADD https://github.com/Yelp/dumb-init/releases/download/v1.0.0/dumb-init_1.0.0_amd64 /usr/local/bin/dumb-init
RUN chmod +x /usr/local/bin/*

ENTRYPOINT [ "dumb-init" ]
VOLUME [ "/data" ]
CMD [ "vpnbot", "-logtostderr", "-config=/data/config.yml" ]

# Configuration file should go into a separate data folder that should be mounted
# at /data; run the container with a user that can write to this folder, otherwise
# channel configuration and tempban synchronization will fail.

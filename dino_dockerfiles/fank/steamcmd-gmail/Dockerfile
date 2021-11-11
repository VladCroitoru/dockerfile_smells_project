FROM golang:latest

MAINTAINER Florian Kinder <florian.kinder@fankserver.com>

# Install dependencies
RUN apt-get update &&\
	apt-get install --no-install-recommends --no-install-suggests -y curl lib32gcc1 &&\
	rm -rf /var/lib/apt/lists/*

# Download and extract SteamCMD
RUN mkdir -p /opt/steamcmd &&\
	cd /opt/steamcmd &&\
	curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -vxz

# Compile application
RUN mkdir -p /go/src/github.com/fank/docker-steamcmd-gmail
ADD . /go/src/github.com/fank/docker-steamcmd-gmail
WORKDIR /go/src/github.com/fank/docker-steamcmd-gmail
RUN go get ./... &&\
	go install github.com/fank/docker-steamcmd-gmail &&\
	cp client_secret.json /client_secret.json &&\
	rm /go/src/* -rf

# This container will be executable
ENTRYPOINT ["/go/bin/docker-steamcmd-gmail"]

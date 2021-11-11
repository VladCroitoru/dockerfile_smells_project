###################################################################################
# Dockerfile to build a Polymer-CLI, Go and firebase  Dev Environment container   #
# Based on node:4-slim                                                            #
#                                                                                 #
# To build, do:                                                                   #
#   $ docker build -t  xn0px90/docker-go-polymer-firebase                         #
# To pull do:                                                                     #
#   $ docker pull xn0px90/docker-go-polymer-firebase                              #
###################################################################################

# Set the base image to node:4-slim
FROM node:4-slim

MAINTAINER xn0px90 <xn0px90@gmail.com>

ENV POLYMER_CLI_HOME /home/polymer
ARG user=polymer
ARG group=polymer
ARG uid=1000
ARG gid=1000

RUN groupadd -g ${gid} ${group} \
    && useradd -d "$POLYMER_CLI_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && \
    npm install -g gulp bower polymer-cli generator-polymer-init-custom-build firebase-tools

    #install Go

ENV GOLANG_VERSION 1.7.1
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz
ENV GOLANG_DOWNLOAD_SHA256 43ad621c9b014cde8db17393dc108378d37bc853aa351a6c74bf6432c1bbd182

RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \
	&& echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c - \
	&& tar -C /usr/local -xzf golang.tar.gz \
	&& rm golang.tar.gz

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
WORKDIR $GOPATH

COPY go-wrapper /usr/local/bin/

RUN go get github.com/derekparker/delve/cmd/dlv

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER ${user}

EXPOSE 8080

RUN mkdir -p /home/${user}/app

VOLUME /home/${user}/app

WORKDIR /home/${user}/app

CMD bash

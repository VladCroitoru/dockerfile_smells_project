FROM alpine:latest

RUN apk update
RUN apk upgrade
RUN apk add --no-cache bash git curl wget jq make

RUN git clone https://github.com/fsaintjacques/semver-tool.git
RUN cd semver-tool && make install

COPY scripts/ /opt/resource/
RUN chmod +x /opt/resource/*

RUN apk del git make

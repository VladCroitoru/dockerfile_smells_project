FROM debian:7

MAINTAINER Geert-Johan Riemer

ADD / gopath/src/github.com/GeertJohan/aerospike-discovery

RUN \
	echo "\033[1;34m >> Install dependencies and tools from apt\033[0m" \
	&& apt-get update -y \
	&& apt-get install -y \
		python \
		ca-certificates git wget \
		--no-install-recommends \
	&& echo "\033[1;34m >> Download and install aerospike tools\033[0m" \
	&& wget --no-verbose "http://www.aerospike.com/download/tools/latest/artifact/debian7" -O aerospike-tools.tgz \
	&& mkdir aerospike-tools \
	&& tar zxf aerospike-tools.tgz --strip-components=1 -C aerospike-tools \
	&& dpkg -i aerospike-tools/aerospike-tools-*.deb \
	&& echo "\033[1;34m >> Download, install and setup go\033[0m" \
	&& wget --no-verbose "https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz" -O go.tar.gz \
	&& tar zxf go.tar.gz -C /usr/local \
	&& export GOPATH="$(pwd)gopath" \
	&& export PATH="$PATH:/usr/local/go/bin" \
	&& mkdir gopath/pkg \
	&& mkdir gopath/bin \
	&& echo "\033[1;34m >> Build and install aerospike-discovery\033[0m" \
	&& cd gopath/src/github.com/GeertJohan/aerospike-discovery \
	&& go get \
	&& go build \
	&& mv aerospike-discovery /usr/local/bin \
	&& cd / \
	&& echo "\033[1;34m >> Remove garbage files and tools\033[0m" \
	&& apt-get purge -y --auto-remove ca-certificates git wget \
	&& rm -rf aerospike-tools.tgz go.tar.gz aerospike-tools gopath /usr/local/go /var/lib/apt/lists/* \
	&& echo "\033[1;34m >> Build complete\033[0m" \

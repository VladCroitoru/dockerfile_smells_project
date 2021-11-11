FROM golang:1.8
MAINTAINER Howard Stark <howard@getcoffee.io>

ARG BUILD_DATE
ARG VCS_REF

ARG PROTOC_VERSION=3.3.0
ARG PROTOC_URL=https://github.com/google/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-x86_64.zip

RUN apt-get update && apt-get install -y --no-install-recommends \
		apt-utils \ 
		curl \
		wget \
		openssl \
		unzip \
	&& rm -rf /var/lib/apt/lists/*

RUN cd / \
    && wget -q "${PROTOC_URL}" -O protoc.zip \
	&& cd /usr \
	&& unzip /protoc.zip \
	&& rm -rf /protoc.zip \
	&& rm -rf /usr/readme.txt \
	&& apt-get purge -y unzip \
	&& apt-get purge -y apt-utils \



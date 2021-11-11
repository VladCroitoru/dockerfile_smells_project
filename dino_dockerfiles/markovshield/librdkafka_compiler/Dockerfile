FROM debian:jessie

MAINTAINER Philip Schmid

ENV LIBRDKAFKA_VERSION=v0.9.5

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		gcc \
		libpcre3-dev \
    apt-utils \
		make \
		git \
		g++ \
		python \
    pkg-config \
		build-essential \
		libsasl2-2 \
    libsasl2-dev \
		openssl \
    libcrypto++9 \
    liblz4-dev \
    liblz4-1 \
		zlib1g-dev \
		zlibc \
	&& rm -r /var/lib/apt/lists/*

WORKDIR /tmp
RUN git config --global http.sslVerify false
RUN git clone https://github.com/edenhill/librdkafka
WORKDIR /tmp/librdkafka
RUN git checkout tags/${LIBRDKAFKA_VERSION}
RUN ./configure
RUN make
